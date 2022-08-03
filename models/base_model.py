#!/usr/bin/env python3
""" This module contains the base class for all the subclasses
"""

from uuid import uuid4
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Base class for all models
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, id=None, created_at=None, updated_at=None):
        """ The init method for base class
        """
        if id is None:
            self.id = BaseModel.id
        if created_at is None:
            self.created_at = BaseModel.created_at
        if updated_at is None:
            self.updated_at = BaseModel.updated_at

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
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """ save method for objects updates
        """
        self.updated_at = datetime.now()
