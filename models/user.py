#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import Place

env = getenv("HBNB_TYPE_STORAGE")
class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    if env == 'db':
        pass
    else:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
  