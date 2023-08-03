#!/usr/bin/python3
""" This module defines a class to manage db storage for hbnb clone """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


class DBStorage:
    """ This class manages storage of hbnb models with a database """
    
