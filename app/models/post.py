from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Post(Base):
    text = Column(Text, nullable=False)
    likes = Column(Integer, nullable=False)
    subscription_id = Column(Integer, ForeignKey('subscription.id'))
    source_id = Column(Integer, ForeignKey('source.id'))

    subscription = relationship('Subscription', back_populates='posts')
    source = relationship('Source', back_populates='posts')
