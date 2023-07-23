from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.digest import Digest


class CRUDDigest(CRUDBase):

    async def get_all_digests_for_user(
        self,
        user_id,
        session: AsyncSession,
    ):
        digests = await session.execute(
            select(Digest).where(
                Digest.user_id == user_id
            )
        )
        return digests.scalars().all()


digest_crud = CRUDDigest(Digest)
