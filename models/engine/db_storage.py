#!/usr/bin/python3
"""
this module define a class to manage Db storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base


class DBStorage:
    """
    this class manages storage of hbnb models
    Private class attributes:
        __engine: set to None
        __session: set to None
    """

    valid_classes = {"Amenity": Amenity, "City": City,
                     "Place": Place, "Review": Review,
                     "State": State, "User": User}
    orm_mapped_classes = {
        "City": City,
        "State": State,
        "User": User
    }
    __engine = None
    __session = None

    def __init__(self):
        """
        method contructor
        Public instance methods:
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, password, host, database),
                                      pool_pre_ping=True)

        environment = getenv("HBNB_ENV")
        if environment == 'test':
            """delete all table in database"""
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries on the current database session,
        objects depending of the class
        """
        obj = {}
        if cls is not None:
            result = self.__session.query(cls)
            for item in result:
                key = "{}.{}".format(item.__class__.__name__, item.id)
                obj[key] = item
        else:
            for cls in self.orm_mapped_classes.values():
                result = self.__session.query(cls).all()
                for item in result:
                    key = "{}.{}".format(item.__class__.__name__, item.id)
                    obj[key] = item
        return obj

    def new(self, obj):
        """
        adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        creates all tables in the database, and
        creates the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        session_needed = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_needed)
        self.__session = Session
