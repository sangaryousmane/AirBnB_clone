#!/usr/bin/env python3
"""
BaseModel - this class serves as a super class to all classes.
Subclasses will inherit from this throughout in this project
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base class for all future classes"""

    def __init__(self, *args, **kwargs):
        """ The class constructor"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Print a nice string representation of the class.
        """

        return f'[{self.name}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at with -
        the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values -
        of __dict__ of the instance
        """
        class_dict = {**self.__dict__}
        class_dict["__class__"] = type(self).__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()

        return class_dict
