from fastapi import APIRouter

from src.api.config import settings
from src.api.endpoints.challenge import router as challenge_router
from src.api.endpoints.images import router as images_router
from src.api.endpoints.votes import router as votes_router

routers = APIRouter(prefix=settings.API_V1_STR)
router_list = [challenge_router, images_router, votes_router]

for router in router_list:
    routers.include_router(router)
