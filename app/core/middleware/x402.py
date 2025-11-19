import os
from fastapi import FastAPI
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from x402.fastapi.middleware import require_payment
from x402.facilitator import FacilitatorConfig

load_dotenv()

# Get payment address (required)
ADDRESS = os.getenv("ADDRESS")
if not ADDRESS:
    raise ValueError("ADDRESS environment variable is required for payment middleware")

# Get facilitator URL (defaults to x402.org public facilitator)
FACILITATOR_URL = os.getenv("FACILITATOR_URL", "https://facilitator.x402.org")

# Create facilitator config
facilitator_config = FacilitatorConfig(url=FACILITATOR_URL)


def apply_payment_middleware(app: FastAPI):
    """Extract payment config from decorated endpoints and apply middleware"""
    for route in app.routes:
        if isinstance(route, APIRoute) and hasattr(route.endpoint, "x402_config"):
            config = route.endpoint.x402_config

            # Build output_schema with query params schema
            output_schema = None
            if config.get("query_params"):
                output_schema = {"input": {"query_params": config["query_params"]}}

            app.middleware("http")(
                require_payment(
                    path=route.path,
                    price=config["price"],
                    pay_to_address=ADDRESS,
                    network="base",
                    description=config.get("description", ""),
                    output_schema=output_schema,
                    discoverable=False,
                    facilitator_config=facilitator_config,
                )
            )
