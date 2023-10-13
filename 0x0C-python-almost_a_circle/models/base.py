#!/usr/bin/python3
import csv
"""base model class"""


class Base:
    """base class model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a Base
        args:
        id (int): id of the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
