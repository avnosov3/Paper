from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.post import post_crud
from app.schemas.post import PostCreateSchema
from app.api.v1.validators import check_obj_exists
from app.crud.source import source_crud
from app import constants


post_router = APIRouter()


@post_router.post('/{source_id}')
async def create_subscription(
    source_id: str,
    post_in: PostCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    await check_obj_exists(
        source_id,
        source_crud,
        constants.SOURCE_NOT_FOUND.format(source_id),
        session
    )
    return await post_crud.create(post_in, session, source_id)
