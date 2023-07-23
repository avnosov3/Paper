from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_

from app.crud.base import CRUDBase
from app.models.subscription import Subscription


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


subscription_crud = CRUDSubscription(Subscription)
