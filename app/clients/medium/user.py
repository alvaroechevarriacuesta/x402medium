from app.clients.medium.base import medium_request

async def get_user_by_username(username: str):
    path = f"/user/id_for/{username}"
    return await medium_request(path, method="GET")