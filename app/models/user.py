from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    name = Column(String, nullable=False)
