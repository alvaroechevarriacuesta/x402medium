from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.user import get_user_by_username as fetch_user_by_username
from app.clients.medium.user import get_user_articles as fetch_user_articles
from app.clients.medium.user import get_user_info as fetch_user_info
from app.clients.medium.user import get_user_top_articles as fetch_user_top_articles
from app.clients.medium.user import get_user_following as fetch_user_following
from app.clients.medium.user import (
    get_user_publication_following as fetch_user_publication_following,
)
from app.clients.medium.user import get_user_followers as fetch_user_followers
from app.clients.medium.user import get_user_interests as fetch_user_interests
from app.clients.medium.user import get_user_lists as fetch_user_lists
from app.clients.medium.user import get_user_publications as fetch_user_publications
from app.clients.medium.user import get_user_books as fetch_user_books


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/id_for")
async def get_user(request: Request):
    params = request.query_params
    username = params.get("username")
    if username is None:
        raise HTTPException(status_code=400, detail="username is required")
    return await fetch_user_by_username(username)


@router.get("/articles")
async def get_user_articles(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = params.get("next", None)
    return await fetch_user_articles(user_id, next)


@router.get("/top_articles")
async def get_user_top_articles(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_top_articles(user_id)


@router.get("/following")
async def get_user_following(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = params.get("next", None)
    return await fetch_user_following(user_id, next)


@router.get("/publication_following")
async def get_user_publication_following(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = params.get("next", None)
    return await fetch_user_publication_following(user_id, next)


@router.get("/followers")
async def get_user_followers(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = params.get("next", None)
    count = params.get("count", None)
    return await fetch_user_followers(user_id, next, count)


@router.get("/interests")
async def get_user_interests(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_interests(user_id)


@router.get("/lists")
async def get_user_lists(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_lists(user_id)


@router.get("/publications")
async def get_user_publications(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_publications(user_id)


@router.get("/books")
async def get_user_books(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_books(user_id)


@router.get("")
async def get_user_info(request: Request):
    params = request.query_params
    user_id = params.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_info(user_id)
