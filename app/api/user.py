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

from app.core.middleware.payment import x402


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/id_for")
@x402(
    price="0.01",
    description="Get the user_id for a username on Medium",
    body_fields={
        "username": {
            "type": "string",
            "description": "The username of the user to get the user_id for",
            "required": True,
        }
    },
)
async def get_user(request: Request):
    body = await request.json()
    username = body.get("username")
    if username is None:
        raise HTTPException(status_code=400, detail="username is required")
    return await fetch_user_by_username(username)


@router.post("/articles")
@x402(
    price="0.01",
    description="Get articles for a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get articles for",
            "required": True,
        },
        "next": {
            "type": "string",
            "description": "Pagination cursor for next page of results",
            "required": False,
        },
    },
)
async def get_user_articles(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = body.get("next", None)
    return await fetch_user_articles(user_id, next)


@router.post("/top_articles")
@x402(
    price="0.01",
    description="Get top articles for a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get top articles for",
            "required": True,
        }
    },
)
async def get_user_top_articles(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_top_articles(user_id)


@router.post("/following")
@x402(
    price="0.01",
    description="Get users followed by a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get following for",
            "required": True,
        },
        "next": {
            "type": "string",
            "description": "Pagination cursor for next page of results",
            "required": False,
        },
    },
)
async def get_user_following(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = body.get("next", None)
    return await fetch_user_following(user_id, next)


@router.post("/publication_following")
@x402(
    price="0.01",
    description="Get publications followed by a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get publication following for",
            "required": True,
        },
        "next": {
            "type": "string",
            "description": "Pagination cursor for next page of results",
            "required": False,
        },
    },
)
async def get_user_publication_following(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = body.get("next", None)
    return await fetch_user_publication_following(user_id, next)


@router.post("/followers")
@x402(
    price="0.01",
    description="Get followers of a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get followers for",
            "required": True,
        },
        "next": {
            "type": "string",
            "description": "Pagination cursor for next page of results",
            "required": False,
        },
        "count": {
            "type": "string",
            "description": "Number of followers to retrieve",
            "required": False,
        },
    },
)
async def get_user_followers(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    next = body.get("next", None)
    count = body.get("count", None)
    return await fetch_user_followers(user_id, next, count)


@router.post("/interests")
@x402(
    price="0.01",
    description="Get interests of a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get interests for",
            "required": True,
        }
    },
)
async def get_user_interests(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_interests(user_id)


@router.post("/lists")
@x402(
    price="0.01",
    description="Get lists created by a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get lists for",
            "required": True,
        }
    },
)
async def get_user_lists(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_lists(user_id)


@router.post("/publications")
@x402(
    price="0.01",
    description="Get publications created by a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get publications for",
            "required": True,
        }
    },
)
async def get_user_publications(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_publications(user_id)


@router.post("/books")
@x402(
    price="0.01",
    description="Get books created by a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get books for",
            "required": True,
        }
    },
)
async def get_user_books(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_books(user_id)


@router.post("")
@x402(
    price="0.01",
    description="Get detailed information about a Medium user",
    body_fields={
        "user_id": {
            "type": "string",
            "description": "The user_id of the user to get info for",
            "required": True,
        }
    },
)
async def get_user_info(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")
    return await fetch_user_info(user_id)
