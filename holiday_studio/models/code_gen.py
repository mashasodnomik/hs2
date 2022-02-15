# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase

metadata = SqlAlchemyBase.metadata


class Order(SqlAlchemyBase):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    title = Column(String)
    describtion = Column(String)


class Client(SqlAlchemyBase):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True)


class Employee(SqlAlchemyBase):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Position(SqlAlchemyBase):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    describtion = Column(String)
    oklad = Column(Float)


class ClientOrder(SqlAlchemyBase):
    __tablename__ = 'client_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_client = Column(ForeignKey('client.id'), nullable=False)
    id_order = Column(ForeignKey('Order.id'), nullable=False)

    client = relationship('Client')
    Order = relationship('Order')


class EmployeeOrder(SqlAlchemyBase):
    __tablename__ = 'employee_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(ForeignKey('employee.id'), nullable=False)
    id_order = Column(ForeignKey('Order.id'), nullable=False)

    employee = relationship('Employee')
    Order = relationship('Order')


class EmployeePosition(SqlAlchemyBase):
    __tablename__ = 'employee_position'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(ForeignKey('employee.id'), nullable=False)
    id_position = Column(ForeignKey('position.id'), nullable=False)

    employee = relationship('Employee')
    position = relationship('Position')
