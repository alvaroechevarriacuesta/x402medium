from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.article import get_article_by_id as fetch_article
from app.clients.medium.article import get_article_content as fetch_article_content
from app.clients.medium.article import get_article_markdown as fetch_article_markdown
from app.clients.medium.article import get_article_html as fetch_article_html
from app.clients.medium.article import get_article_assets as fetch_article_assets
from app.clients.medium.article import get_article_responses as fetch_article_responses
from app.clients.medium.article import get_article_fans as fetch_article_fans
from app.clients.medium.article import (
    get_article_recommended as fetch_article_recommended,
)
from app.clients.medium.article import get_article_related as fetch_article_related
from app.core.middleware.payment import x402

router = APIRouter(prefix="/article", tags=["article"])


@router.post("/content")
@x402(
    price="0.01",
    description="Get the content of a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get content for",
            "required": True,
        }
    },
)
async def get_article_content(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_content(article_id)


@router.post("/markdown")
@x402(
    price="0.01",
    description="Get the markdown of a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get markdown for",
            "required": True,
        }
    },
)
async def get_article_markdown(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_markdown(article_id)


@router.post("/html")
@x402(
    price="0.01",
    description="Get the html of a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get html for",
            "required": True,
        }
    },
)
async def get_article_html(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_html(article_id)


@router.post("/assets")
@x402(
    price="0.01",
    description="Get the assets of a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get assets for",
            "required": True,
        }
    },
)
async def get_article_assets(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_assets(article_id)


@router.post("/responses")
@x402(
    price="0.01",
    description="Get the responses of a Medium article. Note that these responses are considered articles themselves",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get responses for",
            "required": True,
        }
    },
)
async def get_article_responses(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_responses(article_id)


@router.post("/fans")
@x402(
    price="0.01",
    description="Get the fans (user_ids) of a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get fans for",
            "required": True,
        }
    },
)
async def get_article_fans(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_fans(article_id)


@router.post("/recommended")
@x402(
    price="0.01",
    description="Get the 10 recommended articles for a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get recommended articles for",
            "required": True,
        }
    },
)
async def get_article_recommended(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_recommended(article_id)


@router.post("/related")
@x402(
    price="0.01",
    description="Get the 4 related articles (article_ids) for a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get related articles for",
            "required": True,
        }
    },
)
async def get_article_related(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article_related(article_id)


@router.post("")
@x402(
    price="0.01",
    description="Get article related information for a Medium article",
    body_fields={
        "article_id": {
            "type": "string",
            "description": "The article_id of the article to get related information for",
            "required": True,
        }
    },
)
async def get_article(request: Request):
    body = await request.json()
    article_id = body.get("article_id")
    if article_id is None:
        raise HTTPException(status_code=400, detail="article_id is required")
    return await fetch_article(article_id)
