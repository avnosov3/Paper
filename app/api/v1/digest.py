from uuid import uuid1

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.validators import check_user_exits
from app.core.db import get_async_session
from app.core.user import UserManager, get_user_manager
from app.crud.digest import digest_crud
from app.crud.subscription import subscription_crud
from app.schemas.digest import DigestCreateSchema
from app.schemas.post import PostResponseSchema

digest_router = APIRouter()


@digest_router.post('/{user_id}', response_model=list[PostResponseSchema])
async def create_digest(
    user_id: int,
    likes_limits: int,
    session: AsyncSession = Depends(get_async_session),
    user_manager: UserManager = Depends(get_user_manager),
):
    user = await check_user_exits(user_id, user_manager)
    subscriptions = await subscription_crud.get_subscriptions_with_posts(
        user_id,
        session
    )
    results_out = []
    uuid = uuid1()
    for subscribe in subscriptions:
        for post in subscribe.posts:
            session.expunge_all()
            if post.likes > likes_limits:
                results_out.append(
                    PostResponseSchema(text=post.text, likes=post.likes)
                )
                digest = DigestCreateSchema(digest_id=uuid)
                await digest_crud.create(
                    digest,
                    session,
                    post_id=post.id,
                    user=user
                )
    return results_out


@digest_router.get('/{user_id}')
async def get_all_generated_digests_for_user(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await digest_crud.get_all_digests_for_user(
        user_id,
        session
    )
