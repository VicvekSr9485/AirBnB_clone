#!/usr/bin/env python3
"""
This module contains the base model
"""

import uuid
import datetime
from __init__ import storage
import json


date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = BaseModel.id
            self.created_at = BaseModel.created_at
            self.updated_at = BaseModel.updated_at
            storage.new(self)
    
    def setattr(self, key, value):
        if key in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.datetime.strptime(value, date_format)
                except ValueError:
                    raise ValueError('Invalid date format: ({}) for {}'.format(value, key))
        super().__setattr__(key, value)

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
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        storage.save()
