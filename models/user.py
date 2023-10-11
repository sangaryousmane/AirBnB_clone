#!/usr/bin/env python3
"""
User - inherits from BaseModel and handles users data
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ inherits from BaseModel and handles users data"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
