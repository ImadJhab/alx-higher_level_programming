#!/usr/bin/python3
"""defines rectagle class"""


class Rectangle:
    """rectganle class"""
    def __init__(self, width=0, height=0):
        """class initalization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
