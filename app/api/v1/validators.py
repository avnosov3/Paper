from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


async def check_obj_duplicate(
    attr_name: str,
    attr_value: str,
    crud,
    message,
    session: AsyncSession,
):
    db_obj = await crud.get_by_attribute(attr_name, attr_value, session)
    if db_obj is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=message
        )