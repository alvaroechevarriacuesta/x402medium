import os
from dotenv import load_dotenv
from app.core.http_client import make_request

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
RAPID_API_HOST = os.getenv("RAPID_API_HOST")


async def medium_request(path: str, method="GET", params=None, data=None):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": RAPID_API_HOST,
    }
    url = f"{BASE_URL}{path}"
    return await make_request(method, url, headers=headers, params=params, json=data)
