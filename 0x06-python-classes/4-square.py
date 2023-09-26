#!/usr/bin/python3
"""defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """nitialize a new instence of square
        args:
        size(int): size of the new square"""
        self.__size = size

    @property
    def size(self):
        """sets the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets value of the size
        args:
        value(int): value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area of  the square
        Return: square area"""
        return self.__size ** 2
