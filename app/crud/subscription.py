from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.crud.base import CRUDBase
from app.models.subscription import Subscription
from app.models.post import Post


class CRUDSubscription(CRUDBase):

    async def subscription_exists(
        self,
        title: str,
        source_id: int,
        user_id: int,
        session: AsyncSession,
    ):
        subscription = await session.scalars(
            select(True).where(
                select(Subscription).where(
                    Subscription.title == title,
                    Subscription.source_id == source_id,
                    Subscription.user_id == user_id
                ).exists()
            )
        )
        return subscription.first()

    async def get_subscriptions_with_posts(
        self,
        user_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(Subscription).where(
                Subscription.user_id == user_id
            ).options(
                joinedload(Subscription.posts).joinedload(Post.source)
            )
        )
        return db_obj.unique().scalars().all()

    async def get_subscription_by_user_id(
        self,
        user_id: int,
        source_id: int,
        session: AsyncSession,
    ):
        subscription = await session.scalars(
            select(Subscription).where(
                Subscription.source_id == source_id,
                Subscription.user_id == user_id
            )
        )
        return subscription.first()


subscription_crud = CRUDSubscription(Subscription)
