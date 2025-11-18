from fastapi import FastAPI
from app.clients.medium.user import get_user_by_username
from app.api.article import router as article_router
from app.api.list import router as list_router
from app.api.publication import router as publication_router
from app.api.platform import router as platform_router
from app.api.search import router as search_router
from app.api.user import router as user_router


app = FastAPI()
app.include_router(article_router)
app.include_router(list_router)
app.include_router(publication_router)
app.include_router(platform_router)
app.include_router(search_router)
app.include_router(user_router)

@app.get("/")
def hello():
    return {"message": "Hello world!"}



