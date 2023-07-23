from fastapi_users import schemas


class UserResponseSchema(schemas.BaseUser[int]):
    name: str


class UserCreateSchema(schemas.BaseUserCreate):
    name: str


class UserUpdateSchema(schemas.BaseUserUpdate):
    name: str | None
