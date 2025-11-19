import os
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

    # Create a single smart middleware that dynamically handles each route
    class SmartPaymentMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request: Request, call_next):
            path = request.url.path

            # Check if this path requires payment
            if path in route_configs:
                config = route_configs[path]
                # Create the payment middleware for THIS specific request
                payment_middleware = require_payment(path=path, **config)
                # Invoke it directly with the ASGI interface
                return await payment_middleware(
                    request.scope, request.receive, request._send
                )

            # No payment required, continue normally
            return await call_next(request)

    # Register only ONE middleware instance
    app.add_middleware(SmartPaymentMiddleware)
