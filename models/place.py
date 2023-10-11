#!/usr/bin/env python3
"""
Place - inherits from the BaseModel and handle require data for places
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ handle data for Places"""

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
    amenity_id = list()
