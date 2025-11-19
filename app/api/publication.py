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

from app.core.middleware.payment import x402


router = APIRouter(prefix="/publication", tags=["publication"])


@router.post("/id_for")
@x402(
    price="0.01",
    description="Get the publication_id for a publication slug on Medium",
    body_fields={
        "publication_slug": {
            "type": "string",
            "description": "The slug of the publication to get the publication_id for",
            "required": True,
        }
    },
)
async def get_publication_id_for(request: Request):
    body = await request.json()
    slug = body.get("publication_slug")
    if slug is None:
        raise HTTPException(status_code=400, detail="publication_slug is required")
    return await fetch_publication_id_for(slug)


@router.post("/articles")
@x402(
    price="0.01",
    description="Get articles for a Medium publication",
    body_fields={
        "publication_id": {
            "type": "string",
            "description": "The publication_id of the publication to get articles for",
            "required": True,
        },
        "from": {
            "type": "string",
            "description": "Date filter for articles from a specific date",
            "required": False,
        },
    },
)
async def get_publication_articles(request: Request):
    body = await request.json()
    publication_id = body.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    from_date = body.get("from", None)
    return await fetch_publication_articles(publication_id, from_date)


@router.post("/newsletter")
@x402(
    price="0.01",
    description="Get newsletter information for a Medium publication",
    body_fields={
        "publication_id": {
            "type": "string",
            "description": "The publication_id of the publication to get newsletter for",
            "required": True,
        }
    },
)
async def get_publication_newsletter(request: Request):
    body = await request.json()
    publication_id = body.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    return await fetch_publication_newsletter(publication_id)


@router.post("")
@x402(
    price="0.01",
    description="Get detailed information about a Medium publication",
    body_fields={
        "publication_id": {
            "type": "string",
            "description": "The publication_id of the publication to get info for",
            "required": True,
        }
    },
)
async def get_publication_info(request: Request):
    body = await request.json()
    publication_id = body.get("publication_id")
    if publication_id is None:
        raise HTTPException(status_code=400, detail="publication_id is required")
    return await fetch_publication_info(publication_id)
