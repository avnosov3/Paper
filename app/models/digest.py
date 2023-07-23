from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Digest(Base):
    digest_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    user = relationship('User', back_populates='digests')
    posts = relationship('Post', back_populates='digests')
