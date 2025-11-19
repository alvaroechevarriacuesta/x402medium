import os
from typing import Callable
from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from dotenv import load_dotenv
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
    # Collect all route configs and pre-create payment handlers
    payment_handlers = {}

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

            route_config = {
                "price": config["price"],
                "pay_to_address": ADDRESS,
                "network": "base",
                "description": config.get("description", ""),
                "input_schema": input_schema,
                "discoverable": True,
                "facilitator_config": facilitator_config,
            }

            path = route.path
            # Pre-create the require_payment handler for this path
            payment_handlers[path] = require_payment(path=path, **route_config)

    # Create a single middleware that routes to appropriate payment handler
    @app.middleware("http")
    async def x402_middleware(request: Request, call_next: Callable):
        path = request.url.path

        # Log headers
        print(f"Request headers: {dict(request.headers)}")

        # Log body - cache it so downstream middlewares can still read it
        body = await request.body()
        print(f"Request body: {body.decode('utf-8') if body else 'Empty'}")

        # Restore body so it can be read again
        async def receive():
            return {"type": "http.request", "body": body}

        request._receive = receive

        print(f"Request path: {path}")

        if path in payment_handlers:
            print(
                f"Path {path} requires payment, delegating to require_payment middleware"
            )
            require_payment_middleware = payment_handlers[path]
            return await require_payment_middleware(request, call_next)

        print(f"Path {path} does not require payment, passing through")
        return await call_next(request)
