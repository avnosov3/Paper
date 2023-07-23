from fastapi import APIRouter

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)

user_router = APIRouter()

user_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_register_router(UserResponseSchema, UserCreateSchema),
    prefix='/auth',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_users_router(UserResponseSchema, UserUpdateSchema),
    prefix='/users',
    tags=['users'],
)
