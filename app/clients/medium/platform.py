from app.clients.medium.base import medium_request


async def get_recommended_feed(tag: str, page: int = 1):
    path = f"/recommended_feed/{tag}"
    return await medium_request(path, method="GET", params={"page": page})


async def get_topfeeds(tag: str, mode: str):
    path = f"/topfeeds/{tag}/{mode}"
    return await medium_request(path, method="GET")


async def get_top_writers(topic_slug: str):
    path = f"/top_writers/{topic_slug}"
    return await medium_request(path, method="GET")


async def get_latest_posts(topic_slug: str, after: str = None):
    path = f"/latestposts/{topic_slug}"
    params = {}
    if after is not None:
        params["after"] = after
    return await medium_request(path, method="GET", params=params)


async def get_related_tags(tag: str):
    path = f"/related_tags/{tag}"
    return await medium_request(path, method="GET")


async def get_tag_info(tag: str):
    path = f"/tag/{tag}"
    return await medium_request(path, method="GET")


async def get_root_tags():
    path = "/root_tags"
    return await medium_request(path, method="GET")


async def get_archived_articles(
    tag: str, year: str = None, month: str = None, next: str = None
):
    path = f"/archived_articles/{tag}"
    params = {}
    if year is not None:
        params["year"] = year
    if month is not None:
        params["month"] = month
    if next is not None:
        params["next"] = next
    return await medium_request(path, method="GET")


async def get_recommended_users(tag: str):
    path = f"/recommended_users/{tag}"
    return await medium_request(path, method="GET")
