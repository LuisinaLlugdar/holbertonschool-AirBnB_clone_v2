#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


env = getenv("HBNB_TYPE_STORAGE")
class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    """ Create class Amenity """
    if env == 'db':
        name = Column(String(128), nullable=False)
        """place_amenities = relationship("Place", secondary=place_amenity,
                                       backref='amenity')"""
    else:
        name = ""
