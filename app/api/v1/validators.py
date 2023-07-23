from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.exceptions import UserNotExists

from app.crud.subscription import subscription_crud
from app.core.user import UserManager
from app import constants


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


async def check_obj_exists(
    obj_id: int,
    crud,
    message,
    session: AsyncSession
):
    db_obj = await crud.get(obj_id, session)
    if db_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message
        )
    return db_obj


async def check_subscrtiption_made_again(
    title: str,
    source_id: int,
    user_id: int,
    session: AsyncSession
):
    subscription = await subscription_crud.subscription_exists(
        title, source_id, user_id, session
    )
    if subscription is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=constants.SUBSCRIPTION_EXISTS.format(title)
        )


async def check_user_exits(
    user_id: int,
    user_manager: UserManager
):
    try:
        user = await user_manager.get(user_id)
    except UserNotExists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=constants.USER_NOT_FOUND.format(user_id)
        )
    return user
