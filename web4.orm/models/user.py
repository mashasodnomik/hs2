from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    about = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    created_date = Column(DateTime, default=datetime.now)

    news = orm.relation("News", back_populates='user')
