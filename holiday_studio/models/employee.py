from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)