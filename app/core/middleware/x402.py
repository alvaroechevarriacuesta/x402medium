import os
from fastapi import FastAPI
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from x402.fastapi.middleware import require_payment
from x402.facilitator import FacilitatorConfig

load_dotenv()
ADDRESS = os.getenv("ADDRESS")
FACILITATOR_URL = os.getenv("FACILITATOR_URL")

# Create facilitator config
facilitator_config = None
if FACILITATOR_URL:
    facilitator_config = FacilitatorConfig(url=FACILITATOR_URL)


def apply_payment_middleware(app: FastAPI):
    """Extract payment config from decorated endpoints and apply middleware"""
    for route in app.routes:
        if isinstance(route, APIRoute) and hasattr(route.endpoint, "x402_config"):
            config = route.endpoint.x402_config

            app.middleware("http")(
                require_payment(
                    path=route.path,
                    price=config["price"],
                    pay_to_address=ADDRESS,
                    network="base",
                    description=config.get("description", ""),
                    discoverable=False,
                    facilitator_config=facilitator_config,
                )
            )
