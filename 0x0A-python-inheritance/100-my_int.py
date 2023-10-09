#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __equal__(self, other):
        """!= is now =="""
        return int(self) != other

    def __negative__(self, other):
        """== is now !="""
        return int(self) == other
