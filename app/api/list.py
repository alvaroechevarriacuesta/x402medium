from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.list import get_list_articles as fetch_list_articles
from app.clients.medium.list import get_list_responses as fetch_list_responses
from app.clients.medium.list import get_list_info as fetch_list_info

router = APIRouter(prefix="/list", tags=["list"])


@router.get("/articles")
async def get_list_articles(request: Request):
    params = request.query_params
    list_id = params.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_articles(list_id)


@router.get("/responses")
async def get_list_responses(request: Request):
    params = request.query_params
    list_id = params.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_responses(list_id)


@router.get("")
async def get_list_info(request: Request):
    params = request.query_params
    list_id = params.get("list_id")
    if list_id is None:
        raise HTTPException(status_code=400, detail="list_id is required")
    return await fetch_list_info(list_id)
