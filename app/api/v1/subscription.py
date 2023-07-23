from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.subscription import subscription_crud
from app.schemas.subscription import SubscriptionCreateSchema
from app.core.user import current_user
from app.models.user import User
from app.crud.source import source_crud
from app.api.v1.validators import check_obj_exists, check_subscrtiption_made_again, check_subscription_exists
from app import constants

subscription_router = APIRouter()


@subscription_router.post('/{source_id}')
async def create_subscription(
    source_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    source = await check_obj_exists(
        source_id,
        source_crud,
        constants.SOURCE_NOT_FOUND.format(source_id),
        session
    )
    await check_subscrtiption_made_again(
        source.title,
        source_id,
        user.id,
        session
    )
    return await subscription_crud.create(
        SubscriptionCreateSchema(title=source.title),
        session,
        source_id,
        user
    )


@subscription_router.get('/')
async def get_all_subsctibtions(
    session: AsyncSession = Depends(get_async_session)
):
    return await subscription_crud.get_all(session)


@subscription_router.delete('/{source_id}')
async def delete_subscription(
    source_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    subscription_db = await check_subscription_exists(
        source_id,
        user.id,
        session
    )
    await subscription_crud.delete(subscription_db, session)
    return dict(detail=constants.SUBSCRIPTION_DELETED)
