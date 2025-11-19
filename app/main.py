from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.api.article import router as article_router
from app.api.list import router as list_router
from app.api.publication import router as publication_router
from app.api.platform import router as platform_router
from app.api.search import router as search_router
from app.api.user import router as user_router
from app.core.middleware.x402 import apply_payment_middleware


app = FastAPI()

app.include_router(article_router)
app.include_router(list_router)
app.include_router(publication_router)
app.include_router(platform_router)
app.include_router(search_router)
app.include_router(user_router)

apply_payment_middleware(app)


@app.get("/")
def hello():
    return {"message": "Hello world!"}
