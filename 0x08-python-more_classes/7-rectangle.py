#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectganle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class initalization"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints string when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances += 1

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

    def area(self):
        """public instance area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return string of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
