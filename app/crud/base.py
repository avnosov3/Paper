from typing import Generic, List, Optional, Type, TypeVar
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.db import Base
from app.models.user import User

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(
        self,
        obj_id: UUID,
        session: AsyncSession
    ) -> Optional[ModelType]:
        return await session.get(self.model, obj_id)

    async def get_all(self, session: AsyncSession) -> List[ModelType]:
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        in_obj: CreateSchemaType,
        session: AsyncSession,
        user: User | None = None,
    ) -> ModelType:
        in_obj_data = in_obj.dict()
        if user is not None:
            in_obj_data['user_id'] = user.id
        db_obj = self.model(**in_obj_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db_obj: ModelType,
        in_obj: UpdateSchemaType,
        session: AsyncSession,
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        update_data = in_obj.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(
        self,
        db_obj: ModelType,
        session: AsyncSession,
    ) -> ModelType:
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_by_attribute(
        self,
        attr_name: str,
        attr_value: str,
        session: AsyncSession,
    ):
        attr = getattr(self.model, attr_name)
        db_obj = await session.execute(
            select(self.model).where(attr == attr_value)
        )
        return db_obj.scalars().first()

    async def get_all_related_obj(
        self,
        related_obj: str,
        session: AsyncSession
    ):
        related_attr = getattr(self.model, related_obj)
        db_obj = await session.execute(
            select(self.model).options(selectinload(related_attr))
        )
        return db_obj.scalars().all()

    async def get_related_obj_by_id(
        self,
        obj_id: UUID,
        related_obj: str,
        session: AsyncSession
    ):
        related_attr = getattr(self.model, related_obj)
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            ).options(selectinload(related_attr))
        )
        return db_obj.scalars().first()
