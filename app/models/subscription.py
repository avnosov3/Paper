from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Subscription(Base):
    title = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='subscriptions')
