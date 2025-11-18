from fastapi import APIRouter, Request, HTTPException
from app.clients.medium.platform import get_recommended_feed as fetch_recommended_feed
from app.clients.medium.platform import get_topfeeds as fetch_topfeeds
from app.clients.medium.platform import get_top_writers as fetch_top_writers
from app.clients.medium.platform import get_latest_posts as fetch_latest_posts
from app.clients.medium.platform import get_related_tags as fetch_related_tags
from app.clients.medium.platform import get_tag_info as fetch_tag_info
from app.clients.medium.platform import get_root_tags as fetch_root_tags
from app.clients.medium.platform import get_archived_articles as fetch_archived_articles
from app.clients.medium.platform import get_recommended_users as fetch_recommended_users

router = APIRouter(prefix="/platform", tags=["platform"])


@router.get("/recommended_feed")
async def get_recommended_feed(request: Request):
    params = request.query_params
    tag = params.get("tag")
    page = params.get("page", 1)
    return await fetch_recommended_feed(tag, page)


@router.get("/topfeeds")
async def get_topfeeds(request: Request):
    params = request.query_params
    tag = params.get("tag")
    mode = params.get("mode")

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    if mode is None:
        raise HTTPException(status_code=400, detail="mode is required")

    # Validate mode
    valid_modes = [
        "hot",
        "new",
        "top_year",
        "top_month",
        "top_week",
        "top_all_time",
    ]
    if mode not in valid_modes:
        raise HTTPException(
            status_code=400, detail=f"mode must be one of: {', '.join(valid_modes)}"
        )

    return await fetch_topfeeds(tag, mode)


@router.get("/top_writers")
async def get_top_writers(request: Request):
    params = request.query_params
    topic_slug = params.get("topic_slug")

    if topic_slug is None:
        raise HTTPException(status_code=400, detail="topic_slug is required")

    return await fetch_top_writers(topic_slug)


@router.get("/latest_posts")
async def get_latest_posts(request: Request):
    params = request.query_params
    topic_slug = params.get("topic_slug")

    if topic_slug is None:
        raise HTTPException(status_code=400, detail="topic_slug is required")

    after = params.get("after", None)
    return await fetch_latest_posts(topic_slug, after)


@router.get("/related_tags")
async def get_related_tags(request: Request):
    params = request.query_params
    tag = params.get("tag")

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    return await fetch_related_tags(tag)


@router.get("/tag")
async def get_tag_info(request: Request):
    params = request.query_params
    tag = params.get("tag")

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    return await fetch_tag_info(tag)


@router.get("/root_tags")
async def get_root_tags(request: Request):
    return await fetch_root_tags()


@router.get("/archived_articles")
async def get_archived_articles(request: Request):
    params = request.query_params
    tag = params.get("tag")
    year = params.get("year", None)
    month = params.get("month", None)
    next = params.get("next", None)

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    # If either year or month is provided, both must be provided and in correct format
    if year is not None or month is not None:
        if year is None or month is None:
            raise HTTPException(
                status_code=400, detail="Both year and month must be provided together"
            )

        if not year.isdigit() or len(year) != 4:
            raise HTTPException(status_code=400, detail="year must be a 4-digit number")

        if not month.isdigit():
            raise HTTPException(status_code=400, detail="month must be a number")
        month_int = int(month)
        if month_int < 1 or month_int > 12:
            raise HTTPException(
                status_code=400, detail="month must be between 1 and 12"
            )

    return await fetch_archived_articles(tag, year, month, next)


@router.get("/recommended_users")
async def get_recommended_users(request: Request):
    params = request.query_params
    tag = params.get("tag")
    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")
    return await fetch_recommended_users(tag)
