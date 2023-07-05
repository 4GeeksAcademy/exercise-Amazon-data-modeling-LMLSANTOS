import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class myEnum(enum.Enum):
    refund="refund"
    paid="paid"
    cancelled="cancelled"

class Product(Base):
    __tablename__ = 'product'
    # Here we define columns for the table product
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    pricing = Column(Float)
    weight = Column(Float)
    color = Column(String(250))

class Customer(Base):
    __tablename__ = 'customer'
    # Here we define columns for the table Customer
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250),unique=True)
    address = Column(String(250), unique=True)
   
class Bill(Base):
    __tablename__ = 'bill'
    # Here we define columns for the table Bill
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    created_at = Column(String(250))
    total_price = Column(Float, nullable=False)
    status = Column(Enum(myEnum))
    

class Shopping_Cart(Base):
    __tablename__ = 'shopping_cart'
    # Here we define columns for the table Shopping Cart.
    # Notice that each column is also a normal Python instance attribute.
    quantity = Column(Integer)
    price = Column(Float)
    product_id = Column(Integer, ForeignKey('product.id'),primary_key=True)
    product = relationship(Product)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship(Customer)
    bill_id = Column(Float, ForeignKey('bill.id'))
    bill = relationship(Bill)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
