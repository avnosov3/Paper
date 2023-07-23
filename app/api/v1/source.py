from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.source import source_crud
from app.schemas.source import SourceCreateSchema
from app.api.v1.validators import check_obj_duplicate
from app import constants

source_router = APIRouter()


@source_router.post('/')
async def create_source(
    source_in: SourceCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    await check_obj_duplicate(
        'title',
        source_in.title,
        source_crud,
        constants.SOURCE_ALREADY_EXISTS.format(source_in.title),
        session
    )
    return await source_crud.create(source_in, session)
