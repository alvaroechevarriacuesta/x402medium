from app.clients.medium.base import medium_request


async def get_list_articles(list_id: str):
    path = f"/list/{list_id}/articles"
    return await medium_request(path, method="GET")


async def get_list_responses(list_id: str):
    path = f"/list/{list_id}/responses"
    return await medium_request(path, method="GET")


async def get_list_info(list_id: str):
    path = f"/list/{list_id}"
    return await medium_request(path, method="GET")
