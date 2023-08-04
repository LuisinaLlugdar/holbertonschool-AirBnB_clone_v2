#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")
class User(BaseModel):
    """This class defines a user by various attributes"""
    if env == 'db':
        pass
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
