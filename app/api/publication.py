from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.publication import (
    get_publication_id_for as fetch_publication_id_for,
)
from app.clients.medium.publication import (
    get_publication_articles as fetch_publication_articles,
)
from app.clients.medium.publication import (
    get_publication_newsletter as fetch_publication_newsletter,
)
from app.clients.medium.publication import (
    get_publication_info as fetch_publication_info,
)


router = APIRouter(prefix="/publication", tags=["publication"])


@router.get("/id_for")
async def get_publication_id_for(request: Request):
    params = request.query_params
    slug = params.get("publication_slug")
    if slug is None:
        raise HTTPException(status_code=400, detail="publication_slug is required")
    return await fetch_publication_id_for(slug)


@router.get("/articles")
async def get_publication_articles(request: Request):
    params = request.query_params
    publication_id = params.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    from_date = params.get("from", None)
    return await fetch_publication_articles(publication_id, from_date)


@router.get("/newsletter")
async def get_publication_newsletter(request: Request):
    params = request.query_params
    publication_id = params.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    return await fetch_publication_newsletter(publication_id)


@router.get("")
async def get_publication_info(request: Request):
    params = request.query_params
    publication_id = params.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    return await fetch_publication_info(publication_id)
