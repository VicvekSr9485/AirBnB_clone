#!/usr/bin/python3
""" This Module defines a class User that inherits from
the BaseModel class"""

from uuid import uuid4
from models.base_model import BaseModel


class User(BaseModel):
    """ class User implements
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
