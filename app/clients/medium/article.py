from app.clients.medium.base import medium_request


async def get_article_by_id(article_id: str):
    path = f"/article/{article_id}"
    return await medium_request(path, method="GET")


async def get_article_content(article_id: str):
    path = f"/article/{article_id}/content"
    return await medium_request(path, method="GET")


async def get_article_markdown(article_id: str):
    path = f"/article/{article_id}/markdown"
    return await medium_request(path, method="GET")


async def get_article_html(article_id: str):
    path = f"/article/{article_id}/html"
    return await medium_request(path, method="GET")


async def get_article_assets(article_id: str):
    path = f"/article/{article_id}/assets"
    return await medium_request(path, method="GET")


async def get_article_responses(article_id: str):
    path = f"/article/{article_id}/responses"
    return await medium_request(path, method="GET")


async def get_article_fans(article_id: str):
    path = f"/article/{article_id}/fans"
    return await medium_request(path, method="GET")


async def get_article_recommended(article_id: str):
    path = f"/article/{article_id}/recommended"
    return await medium_request(path, method="GET")


async def get_article_related(article_id: str):
    path = f"/article/{article_id}/related"
    return await medium_request(path, method="GET")
