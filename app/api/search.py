from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.search import get_search_users as fetch_search_users
from app.clients.medium.search import (
    get_search_publications as fetch_search_publications,
)
from app.clients.medium.search import get_search_articles as fetch_search_articles
from app.clients.medium.search import get_search_tags as fetch_search_tags
from app.clients.medium.search import get_search_lists as fetch_search_lists


router = APIRouter(prefix="/search", tags=["search"])


@router.get("/users")
async def get_search_users(request: Request):
    params = request.query_params
    query = params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_users(query)


@router.get("/publications")
async def get_search_publications(request: Request):
    params = request.query_params
    query = params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_publications(query)


@router.get("/articles")
async def get_search_articles(request: Request):
    params = request.query_params
    query = params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_articles(query)


@router.get("/tags")
async def get_search_tags(request: Request):
    params = request.query_params
    query = params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
    return await fetch_search_tags(query)


@router.get("/lists")
async def get_search_lists(request: Request):
    params = request.query_params
    query = params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="query is required")
