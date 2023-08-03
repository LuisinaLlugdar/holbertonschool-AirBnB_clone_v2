#!/usr/bin/python3
""" This module defines a class to manage db storage for hbnb clone """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """ This class manages storage of hbnb models with a database """
    ___engine = None
    ___session = None

    def __init__(self):
        "initilize DBStorage class"

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)
        
        env = getenv("HBNB_ENV")
        if env == "test":
            Base.metadata.drop_all(self.___engine)

    def all(self, cls=None):
        """query on the current database session"""
        result = {}
        if cls:
            query = self.___session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query = self.___session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return result


           








    
