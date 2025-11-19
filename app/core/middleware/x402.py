import os
from fastapi import FastAPI
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
    for route in app.routes:
        if isinstance(route, APIRoute) and hasattr(route.endpoint, "x402_config"):
            config = route.endpoint.x402_config

            input_schema = None
            if config.get("body_fields"):
                input_schema = HTTPInputSchema(
                    body_type="json", body_fields=config["body_fields"]
                )

            app.middleware("http")(
                require_payment(
                    path=route.path,
                    price=config["price"],
                    pay_to_address=ADDRESS,
                    network="base",
                    description=config.get("description", ""),
                    input_schema=input_schema,
                    discoverable=False,
                    facilitator_config=facilitator_config,
                )
            )
