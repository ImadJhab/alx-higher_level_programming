#!/usr/bin/python3
"""defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """nitialize a new instence of square
        args:
        size(int): size of the new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
