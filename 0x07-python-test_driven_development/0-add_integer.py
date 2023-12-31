#!/usr/bin/python3
"""
0-add integer function
"""


def add_integer(a, b=98):
    """addition two numbers
    args:
    a: first number
    b: second number
    Return: results"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
