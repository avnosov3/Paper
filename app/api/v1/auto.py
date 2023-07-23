from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.source import source_crud
from app.schemas.source import SourceCreateSchema, SourceEnum
from app import constants
from app.core.user import get_user_manager, UserManager
from app.schemas.user import UserCreateSchema
from app.crud.subscription import subscription_crud
from app.models.subscription import Subscription

auto_router = APIRouter()


@auto_router.get('/fill-source')
async def fill_db(
    session: AsyncSession = Depends(get_async_session),
):
    for source in SourceEnum:
        await source_crud.create(
            SourceCreateSchema(title=source.value),
            session
        )
    return dict(detail=constants.SOURCES_FILLED)


@auto_router.get('/fill-user')
async def fill_user(
    user_manager: UserManager = Depends(get_user_manager)
):
    for email, password, name in (
        ('user@example.com', 'string', 'Anton'),
        ('1user@example.com', 'string', 'Egor'),
        ('3user@example.com', 'string', 'Sergey'),
    ):
        await user_manager.create(
            UserCreateSchema(email=email, password=password, name=name)
        )
    return dict(detail=constants.USERS_FILLED)


@auto_router.get('/fill-subscriptions')
async def fill_subscriptions(
    session: AsyncSession = Depends(get_async_session),
):
    for title, user_id, source_id in (
        ('rbk', 1, 1),
        ('rbk', 2, 1),
        ('meduza', 1, 2),
        ('meduza', 3, 2),
        ('ovd-info', 1, 3),
        ('ovd-info', 2, 3),
        ('rt', 1, 4),
        ('rt', 2, 4),
        ('rt', 3, 4),
    ):
        subscription_db = (
            Subscription(title=title, user_id=user_id, source_id=source_id)
        )
        session.add(subscription_db)
        await session.commit()
        await session.refresh(subscription_db)
    return dict(detail=constants.SUBSCRIPTIONS_FILLED)
