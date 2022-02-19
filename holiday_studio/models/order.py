from sqlalchemy import Column, Float, Integer, String
from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    title = Column(String)
    describtion = Column(String)
