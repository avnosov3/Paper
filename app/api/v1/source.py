from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.source import source_crud
from app.schemas.source import SourceCreateSchema
from app.api.v1.validators import check_obj_duplicate, check_obj_exists
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


@source_router.get('/')
async def get_all_sources(
    session: AsyncSession = Depends(get_async_session),
):
    return await source_crud.get_all(session)


@source_router.patch('/{source_id}')
async def update_partially_source(
    source_id: int,
    source_in: SourceCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    source_db = await check_obj_exists(
        source_id,
        source_crud,
        constants.SOURCE_NOT_FOUND.format(source_id),
        session
    )
    return await source_crud.update(source_db, source_in, session)


@source_router.delete('/{source_id}')
async def delete_source(
    source_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    source_db = await check_obj_exists(
        source_id,
        source_crud,
        constants.SOURCE_NOT_FOUND.format(source_id),
        session
    )
    await source_crud.delete(source_db, session)
    return dict(detail=constants.SOURCE_DELETED)
