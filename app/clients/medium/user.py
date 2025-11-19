from app.clients.medium.base import medium_request


async def get_user_by_username(username: str):
    path = f"/user/id_for/{username}"
    return await medium_request(path, method="GET")


async def get_user_info(user_id: str):
    path = f"/user/{user_id}"
    return await medium_request(path, method="GET")


async def get_user_articles(user_id: str, next: str = None):
    path = f"/user/{user_id}/articles"
    params = {}
    if next is not None:
        params["next"] = next
    return await medium_request(path, method="GET", params=params)


async def get_user_top_articles(user_id: str):
    path = f"/user/{user_id}/top_articles"
    return await medium_request(path, method="GET")


async def get_user_following(user_id: str, next: str = None):
    path = f"/user/{user_id}/following"
    params = {}
    if next is not None:
        params["next"] = next
    return await medium_request(path, method="GET", params=params)


async def get_user_publication_following(user_id: str, next: str = None):
    path = f"/user/{user_id}/publication_following"
    params = {}
    if next is not None:
        params["next"] = next
    return await medium_request(path, method="GET", params=params)


async def get_user_followers(user_id: str, after: str = None, count: int = None):
    path = f"/user/{user_id}/followers"
    params = {}
    if after is not None:
        params["after"] = after
    if count is not None:
        if count > 25:
            count = 25
        params["count"] = count
    return await medium_request(path, method="GET", params=params)


async def get_user_interests(user_id: str):
    path = f"/user/{user_id}/interests"
    return await medium_request(path, method="GET")


async def get_user_lists(user_id: str):
    path = f"/user/{user_id}/lists"
    return await medium_request(path, method="GET")


async def get_user_publications(user_id: str):
    path = f"/user/{user_id}/publications"
    return await medium_request(path, method="GET")


async def get_user_books(user_id: str):
    path = f"/user/{user_id}/books"
    return await medium_request(path, method="GET")
