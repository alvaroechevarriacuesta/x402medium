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

from app.core.middleware.payment import x402

router = APIRouter(prefix="/platform", tags=["platform"])


@router.post("/recommended_feed")
@x402(
    price="0.01",
    description="Get recommended feed from Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to filter recommended feed by",
            "required": False,
        },
        "page": {
            "type": "integer",
            "description": "Page number for pagination (defaults to 1)",
            "required": False,
        },
    },
)
async def get_recommended_feed(request: Request):
    body = await request.json()
    tag = body.get("tag")
    page = body.get("page", 1)
    return await fetch_recommended_feed(tag, page)


@router.post("/topfeeds")
@x402(
    price="0.01",
    description="Get top feeds for a tag on Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to get top feeds for",
            "required": True,
        },
        "mode": {
            "type": "string",
            "description": "Mode for top feeds: hot, new, top_year, top_month, top_week, or top_all_time",
            "required": True,
        },
    },
)
async def get_topfeeds(request: Request):
    body = await request.json()
    tag = body.get("tag")
    mode = body.get("mode")

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


@router.post("/top_writers")
@x402(
    price="0.01",
    description="Get top writers for a topic on Medium",
    body_fields={
        "topic_slug": {
            "type": "string",
            "description": "Topic slug to get top writers for",
            "required": True,
        }
    },
)
async def get_top_writers(request: Request):
    body = await request.json()
    topic_slug = body.get("topic_slug")

    if topic_slug is None:
        raise HTTPException(status_code=400, detail="topic_slug is required")

    return await fetch_top_writers(topic_slug)


@router.post("/latest_posts")
@x402(
    price="0.01",
    description="Get latest posts for a topic on Medium",
    body_fields={
        "topic_slug": {
            "type": "string",
            "description": "Topic slug to get latest posts for",
            "required": True,
        },
        "after": {
            "type": "string",
            "description": "Pagination cursor for posts after a certain point",
            "required": False,
        },
    },
)
async def get_latest_posts(request: Request):
    body = await request.json()
    topic_slug = body.get("topic_slug")

    if topic_slug is None:
        raise HTTPException(status_code=400, detail="topic_slug is required")

    after = body.get("after", None)
    return await fetch_latest_posts(topic_slug, after)


@router.post("/related_tags")
@x402(
    price="0.01",
    description="Get related tags for a tag on Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to get related tags for",
            "required": True,
        }
    },
)
async def get_related_tags(request: Request):
    body = await request.json()
    tag = body.get("tag")

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    return await fetch_related_tags(tag)


@router.post("/tag")
@x402(
    price="0.01",
    description="Get detailed information about a tag on Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to get information for",
            "required": True,
        }
    },
)
async def get_tag_info(request: Request):
    body = await request.json()
    tag = body.get("tag")

    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")

    return await fetch_tag_info(tag)


@router.post("/root_tags")
@x402(
    price="0.01",
    description="Get root tags on Medium",
)
async def get_root_tags(request: Request):
    return await fetch_root_tags()


@router.post("/archived_articles")
@x402(
    price="0.01",
    description="Get archived articles for a tag on Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to get archived articles for",
            "required": True,
        },
        "year": {
            "type": "string",
            "description": "Year for archived articles (4-digit, must be provided with month)",
            "required": False,
        },
        "month": {
            "type": "string",
            "description": "Month for archived articles (1-12, must be provided with year)",
            "required": False,
        },
        "next": {
            "type": "string",
            "description": "Pagination cursor for next page of results",
            "required": False,
        },
    },
)
async def get_archived_articles(request: Request):
    body = await request.json()
    tag = body.get("tag")
    year = body.get("year", None)
    month = body.get("month", None)
    next = body.get("next", None)

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


@router.post("/recommended_users")
@x402(
    price="0.01",
    description="Get recommended users for a tag on Medium",
    body_fields={
        "tag": {
            "type": "string",
            "description": "Tag to get recommended users for",
            "required": True,
        }
    },
)
async def get_recommended_users(request: Request):
    body = await request.json()
    tag = body.get("tag")
    if tag is None:
        raise HTTPException(status_code=400, detail="tag is required")
    return await fetch_recommended_users(tag)
