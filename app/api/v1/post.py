from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.post import post_crud
from app.schemas.post import PostCreateSchema
from app.core.user import current_user
from app.models.user import User

post_router = APIRouter()


@post_router.post('/')
async def create_subscription(
    post_in: PostCreateSchema,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    return await post_crud.create(post_in, session)
