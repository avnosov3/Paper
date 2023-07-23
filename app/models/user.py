from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    name = Column(String, nullable=False)

    subscriptions = relationship(
        'Subscription', back_populates='user', cascade='delete'
    )
