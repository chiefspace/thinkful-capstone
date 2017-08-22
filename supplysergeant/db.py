from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, relationship, ForeignKey

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    assignee = Column(String(80))
    date_assigned = Column(DateTime, default=datetime.datetime.now)
    cost = Column(Float(precision=2))

    inventory_id = Column(Integer, ForeignKey('inventories.id'))
    inventory = relationship('InventoryModel')
    
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    email = Column(String(80), unique=True)
    password = Column(String(80))


Base.metadata.create_all(engine)
