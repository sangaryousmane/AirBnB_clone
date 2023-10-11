#!/usr/bin/env python3
""""
State - inherits from the BaseModel and handles the state related data
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Store the state related info"""

    name = ""
