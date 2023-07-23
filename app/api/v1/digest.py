from uuid import uuid1

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.api.v1.validators import check_user_exits
from app.core.user import get_user_manager, UserManager
from app.crud.subscription import subscription_crud
from app.schemas.post import PostResponseSchema
from app.schemas.digest import DigestCreateSchema
from app.crud.digest import digest_crud

digest_router = APIRouter()


@digest_router.post('/{user_id}', response_model=list[PostResponseSchema])
async def get_digest(
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
