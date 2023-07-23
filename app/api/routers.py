from fastapi import APIRouter

from app.api.v1.routers import api_router_v1
from app.api.user import user_router

main_router_v1 = APIRouter()
main_router_v1.include_router(api_router_v1)
main_router_v1.include_router(user_router)
