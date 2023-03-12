from fastapi import APIRouter

from be.api.api_v1.endpoints import images

api_router = APIRouter()
api_router.include_router(images.router, prefix="/images", tags=["Images"])