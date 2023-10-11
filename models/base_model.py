#!/usr/bin/python3
"""This Model defines all common attributes/methods
for other classes. Its goal is to take care of initialization,
serialization and deserialization of future instances
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel - this class serves as a super class to all classes.
       Subclasses will inherit from this throughout in this project
    """

    def __init__(self, *args, **kwargs):
        """Initialize id, create_at, and updated_at
        public instance attribute

        args:
            *args => list of args, positional args
            **kwargs => key, values pairs
        """

        if kwargs:
            # we are creating an instance from a dictionary
            for key, value in kwargs.items():
                if key != '__class__':
                    # if key is not __class__ then check if it is
                    # created_at or updated_at convert the string
                    # rep to datetime object using datetime.strptime()
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime
                                (value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            # we are creating a new instance from the beginning
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print a nice string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Create and return a dictionary representation
           of the instance's attributes
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime(
                                    '%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime(
                                    '%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict

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
