from functools import wraps
from typing import Dict, Any, Optional


def x402(
    price: str,
    description: str,
    body_fields: Optional[Dict[str, Any]] = None,
):
    """
    Decorator to add x402 payment requirements to an endpoint

    Args:
        price: Payment price (e.g., "$0.001", "10000" for tokens)
        description: Description of what is being purchased
        body_fields: Schema for JSON body fields
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        wrapper.x402_config = {
            "price": price,
            "description": description,
            "body_fields": body_fields,
        }
        return wrapper

    return decorator
