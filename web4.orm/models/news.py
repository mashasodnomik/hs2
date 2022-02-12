from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    is_private = Column(Boolean, nullable=False, server_default=text("0"))
    user_id = Column(ForeignKey('users.id'))

    user = relationship('User')