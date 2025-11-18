from app.clients.medium.base import medium_request


async def get_search_users(query: str):
    path = f"/search/users"
    params = {"query": query}
    return await medium_request(path, method="GET", params=params)


async def get_search_publications(query: str):
    path = f"/search/publications"
    params = {"query": query}
    return await medium_request(path, method="GET", params=params)


async def get_search_articles(query: str):
    path = f"/search/articles"
    params = {"query": query}
    return await medium_request(path, method="GET", params=params)


async def get_search_tags(query: str):
    path = f"/search/tags"
    params = {"query": query}
    return await medium_request(path, method="GET", params=params)


async def get_search_lists(query: str):
    path = f"/search/lists"
    params = {"query": query}
    return await medium_request(path, method="GET", params=params)
