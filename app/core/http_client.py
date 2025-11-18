import httpx

client = httpx.AsyncClient(timeout=15.0)


async def make_request(method: str, url, **kwargs):
    response = await client.request(method, url, **kwargs)
    response.raise_for_status()
    return response.json()
