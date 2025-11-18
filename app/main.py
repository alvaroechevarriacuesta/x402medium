from fastapi import FastAPI
from app.clients.medium.user import get_user_by_username

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello world!"}


@app.get("/user/{username}")
async def get_user(username: str):
    """Get Medium user by username"""
    return await get_user_by_username(username)
