#!/usr/bin/python3
"""
file storage module
"""

from models.base_model import BaseModel
import json
import os
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Classes for file storage models
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all objects in the storage
        """
        return self.__objects

    def new(self, obj):
        """ Create a new object in the storage
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """ Save the object in the storage
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
            json.dump(new_dict, open(self.__file_path, "w"))

    def reload(self):
        """ Reload the object in the storage
        """
        if os.path.exists(self.__file_path):
            new_data = json.load(open(self.__file_path, "r"))
            for key, value in new_data.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
