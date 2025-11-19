from functools import wraps
from typing import Dict, Any, Optional


def x402(
    price: str,
    description: str,
    query_params: Optional[Dict[str, Any]] = None,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.x402_config = {
            "price": price,
            "description": description,
            "query_params": query_params,
        }
        return wrapper

    return decorator
