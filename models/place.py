#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")
class Place(BaseModel):
    """ A place to stay """
    if env == 'db':
        pass
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
