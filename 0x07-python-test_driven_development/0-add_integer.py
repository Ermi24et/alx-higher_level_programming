#!/usr/bin/python3

""" module that adds two numbers
example:
add_integer(3, 2)
5
"""


def add_integer(a, b=98):
    """ 
    function that adds two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
