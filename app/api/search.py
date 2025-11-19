from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.search import get_search_users as fetch_search_users
from app.clients.medium.search import (
    get_search_publications as fetch_search_publications,
)
from app.clients.medium.search import get_search_articles as fetch_search_articles
from app.clients.medium.search import get_search_tags as fetch_search_tags
from app.clients.medium.search import get_search_lists as fetch_search_lists

from app.core.middleware.payment import x402


router = APIRouter(prefix="/search", tags=["search"])


@router.post("/users")
@x402(
    price="0.01",
    description="Search for users on Medium",
    body_fields={
        "query": {
            "type": "string",
            "description": "The search query to find users",
            "required": True,
        }
    },
)
async def get_search_users(request: Request):
    body = await request.json()
    query = body.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_users(query)


@router.post("/publications")
@x402(
    price="0.01",
    description="Search for publications on Medium",
    body_fields={
        "query": {
            "type": "string",
            "description": "The search query to find publications",
            "required": True,
        }
    },
)
async def get_search_publications(request: Request):
    body = await request.json()
    query = body.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_publications(query)


@router.post("/articles")
@x402(
    price="0.01",
    description="Search for articles on Medium",
    body_fields={
        "query": {
            "type": "string",
            "description": "The search query to find articles",
            "required": True,
        }
    },
)
async def get_search_articles(request: Request):
    body = await request.json()
    query = body.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_articles(query)


@router.post("/tags")
@x402(
    price="0.01",
    description="Search for tags on Medium",
    body_fields={
        "query": {
            "type": "string",
            "description": "The search query to find tags",
            "required": True,
        }
    },
)
async def get_search_tags(request: Request):
    body = await request.json()
    query = body.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_tags(query)


@router.post("/lists")
@x402(
    price="0.01",
    description="Search for lists on Medium",
    body_fields={
        "query": {
            "type": "string",
            "description": "The search query to find lists",
            "required": True,
        }
    },
)
async def get_search_lists(request: Request):
    body = await request.json()
    query = body.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_lists(query)
