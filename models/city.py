#!/usr/bin/python3
"""
City - inherits from the BaseModel and handle city data
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ store city related data"""
    state_id = ""
    name = ""
