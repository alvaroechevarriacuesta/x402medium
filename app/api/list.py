from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.list import get_list_articles as fetch_list_articles
from app.clients.medium.list import get_list_responses as fetch_list_responses
from app.clients.medium.list import get_list_info as fetch_list_info

from app.core.middleware.payment import x402

router = APIRouter(prefix="/list", tags=["list"])


@router.post("/articles")
@x402(
    price="0.01",
    description="Get articles in a Medium list",
    body_fields={
        "list_id": {
            "type": "string",
            "description": "The list_id of the list to get articles for",
            "required": True,
        }
    },
)
async def get_list_articles(request: Request):
    body = await request.json()
    list_id = body.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_articles(list_id)


@router.post("/responses")
@x402(
    price="0.01",
    description="Get responses to a Medium list",
    body_fields={
        "list_id": {
            "type": "string",
            "description": "The list_id of the list to get responses for",
            "required": True,
        }
    },
)
async def get_list_responses(request: Request):
    body = await request.json()
    list_id = body.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_responses(list_id)


@router.post("")
@x402(
    price="0.01",
    description="Get detailed information about a Medium list",
    body_fields={
        "list_id": {
            "type": "string",
            "description": "The list_id of the list to get info for",
            "required": True,
        }
    },
)
async def get_list_info(request: Request):
    body = await request.json()
    list_id = body.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_info(list_id)
