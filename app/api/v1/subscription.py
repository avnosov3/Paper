from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.subscription import subscription_crud
from app.schemas.subscription import SubscriptionCreateSchema
from app.core.user import current_user
from app.models.user import User

subscription_router = APIRouter()


@subscription_router.post('/')
async def create_subscription(
    subscription_in: SubscriptionCreateSchema,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    return await subscription_crud.create(subscription_in, session, user)
