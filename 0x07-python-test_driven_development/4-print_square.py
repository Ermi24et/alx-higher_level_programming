#!/usr/bin/python3

""" a module that prints a square with char '#'
example:
    print_square(1)
    #
"""


def print_square(size):
    """
    a function that prints a square with char '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
