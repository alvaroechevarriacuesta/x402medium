from fastapi import APIRouter
from app.clients.medium.user import get_user_by_username


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{username}")
async def get_user(username: str):
    """Get Medium user by username"""
    return await get_user_by_username(username)
