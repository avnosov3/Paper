from fastapi import APIRouter

from app.api.user import user_router

main_router_v1 = APIRouter(prefix='/api/v1')
main_router_v1.include_router(user_router)
