#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")
class Review(BaseModel):
    """ Review classto store review information """
    if env == 'db':
        pass
    else:
        place_id = ""
        user_id = ""
        text = ""
