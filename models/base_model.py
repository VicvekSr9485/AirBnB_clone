#!/usr/bin/env python3
""" This module contains the base class for all the subclasses
"""

from uuid import uuid4
from datetime import datetime
import models

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Base class for all models
    """

    def __init__(self, *args, **kwargs):
        """ The init method for base class
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __setattr__(self, name, value):
        """Maintain correct types for non-string attributes while keeping
        the attributes as public attributes.
        Args:
            name (str): name of attribute
            value: value to associate with `name`
        Raises:
            AttributeError: If value cannot be parsed into correct format
        """
        if name in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    raise AttributeError("Invalid value: ({}) for name: ({})"
                                         .format(value, name))
        super().__setattr__(name, value)

    def to_dict(self):
        """ dictionary representation of the objects
        """
        dict = {}
        dict.update(self.__dict__)
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict

    def __str__(self):
        """ string format method """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ save method for objects updates
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
