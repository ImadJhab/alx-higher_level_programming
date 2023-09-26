#!/usr/bin/python3
"""defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize a new instence of square
        args:
        size(int): size of the new square"""
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sts the value of position
        args:
        value(tuple): tuple of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        area of  the square
        Return: square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
