from fastapi import APIRouter

from api.routes import tasks, auth

api_router = APIRouter()

api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])