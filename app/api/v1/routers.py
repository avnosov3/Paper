from fastapi import APIRouter

from app.api.v1.auto import auto_router
from app.api.v1.digest import digest_router
from app.api.v1.source import source_router
from app.api.v1.subscription import subscription_router

api_router_v1 = APIRouter(prefix='/api/v1')
api_router_v1.include_router(
    auto_router, prefix='/auto', tags=['Auto']
)
api_router_v1.include_router(
    source_router, prefix='/source', tags=['Sources']
)
api_router_v1.include_router(
    subscription_router, prefix='/subscription', tags=['Subscriptions']
)
api_router_v1.include_router(
    digest_router, prefix='/digest', tags=['Digests']
)
