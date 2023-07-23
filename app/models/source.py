from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Source(Base):
    title = Column(String(100), nullable=False, unique=True)

    subscriptions = relationship('Subscription', back_populates='source')
    posts = relationship('Post', back_populates='source')
