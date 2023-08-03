#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """ Establish relationship with City class, using DB as storage method """
    cities = relationship('City', backref='state', cascade='all, delete_orphan')

    @property
    def cities(self, cls=None):
        """ Getter for City instances, using FileStorage as storage method """
        cities_state = []
        instances = models.storage.all(cls)
        for k, elem in instances.items():
            cities_state.append(elem)
        return cities_state
