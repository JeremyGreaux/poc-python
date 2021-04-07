from fastapi import APIRouter

from app.endpoints import users, items

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
api_router.include_router(items.router, tags=["items"])