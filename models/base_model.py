#!/usr/bin/python3
"""This Model defines all common attributes/methods
for other classes. Its goal is to take care of initialization,
serialization and deserialization of future instances
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class for other classes to inherit"""

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

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Create and return a dictionary representation
           of the instance's attributes
        """

        # copy the instance's dictionary &
        # add __class__ key to dict with the class name
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        # convert created_at, updated_at to string using strftime()
        obj_dict['created_at'] = self.created_at.strftime(
                                    '%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime(
                                    '%Y-%m-%dT%H:%M:%S.%f')

        return obj_dict
