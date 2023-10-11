#!/usr/bin/env python3
"""
Amenity - inherits from the BaseModel and handle require data
for all amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ handle data for amenity"""

    name = ""
