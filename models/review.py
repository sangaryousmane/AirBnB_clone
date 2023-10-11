#!/usr/bin/env python3
"""
Review - inherits from the BaseModel and handle require data
for all Reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ handle data for reviews"""

    place_id = ""
    user_id = ""
    text = ""
