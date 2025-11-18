from app.clients.medium.base import medium_request

async def get_publication_id_for(slug: str):
    path = f"/publication/id_for/{slug}"
    return await medium_request(path, method="GET")

async def get_publication_articles(publication_id: str, from_date: str = None):
    path = f"/publication/{publication_id}/articles"
    params = {}
    if from_date is not None:
        params["from"] = from_date
    return await medium_request(path, method="GET", params=params)

async def get_publication_newsletter(publication_id: str):
    path = f"/publication/{publication_id}/newsletter"
    return await medium_request(path, method="GET")

async def get_publication_info(publication_id: str):
    path = f"/publication/{publication_id}"
    return await medium_request(path, method="GET")