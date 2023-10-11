#!/usr/bin/env python3
"""
FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Serialize and deserializes JSON file instances"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ Returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        k = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as writer:
            json.dump(
                {key: value.to_dict()
                 for key, value in FileStorage.__objects.items()}, writer)

    def reload(self):
        """ deserializes the JSON file to
        __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        modules = {
                "BaseModel": BaseModel,
                "User": User, "State": State,
                "City": City, "Amenity": Amenity,
                "Place": Place, "Review": Review
                }

        if not exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as writer:
            d = None

            try:
                d = json.load(writer)
            except json.JSONDecodeError:
                pass

            if d is None:
                return

            FileStorage.__objects = {key: modules[key.split(".")[0]](**value)
                                     for key, value in d.items()}
