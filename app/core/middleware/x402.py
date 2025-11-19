import os
from typing import Callable
from fastapi import FastAPI
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from x402.fastapi.middleware import require_payment
from x402.facilitator import FacilitatorConfig
from x402.types import HTTPInputSchema

load_dotenv()

# Payment configuration
ADDRESS = os.getenv("ADDRESS")
if not ADDRESS:
    raise ValueError("ADDRESS environment variable is required for x402 payments")

FACILITATOR_URL = os.getenv("FACILITATOR_URL", "https://facilitator.x402.org")

facilitator_config = FacilitatorConfig(url=FACILITATOR_URL)


def apply_payment_middleware(app: FastAPI):
    # Collect all route configs first
    route_configs = {}
    for route in app.routes:
        if isinstance(route, APIRoute) and hasattr(route.endpoint, "x402_config"):
            config = route.endpoint.x402_config

            input_schema = None
            body_fields = config.get("body_fields")
            query_params = config.get("query_params")

            # Only create schema if there are actual fields defined (not empty dict)
            has_body_fields = body_fields and len(body_fields) > 0
            has_query_params = query_params and len(query_params) > 0

            if has_body_fields or has_query_params:
                input_schema = HTTPInputSchema(
                    body_type="json" if has_body_fields else None,
                    body_fields=body_fields if has_body_fields else {},
                    query_params=query_params if has_query_params else {},
                    header_fields={},
                )

            route_configs[route.path] = {
                "price": config["price"],
                "pay_to_address": ADDRESS,
                "network": "base",
                "description": config.get("description", ""),
                "input_schema": input_schema,
                "discoverable": True,
                "facilitator_config": facilitator_config,
            }

    # Pre-create payment handlers for each route
    payment_handlers = {}
    for path, config in route_configs.items():
        # require_payment returns a middleware function
        payment_handlers[path] = require_payment(path=path, **config)

    # Create ONE unified middleware that routes to appropriate payment handler
    class UnifiedPaymentMiddleware:
        def __init__(self, handlers: dict):
            self.handlers = handlers

        async def __call__(self, scope, receive, send):
            if scope["type"] != "http":
                # Not HTTP, skip
                return await app.app(scope, receive, send)

            path = scope["path"]

            # Check if this path requires payment
            if path in self.handlers:
                # Delegate to the specific payment handler for this path
                handler = self.handlers[path]
                return await handler(scope, receive, send)

            # No payment required, continue to next middleware/handler
            return await app.app(scope, receive, send)

    # Register ONE middleware instance that handles all routes
    middleware_instance = UnifiedPaymentMiddleware(payment_handlers)
    app.middleware("http")(middleware_instance)
