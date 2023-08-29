#!/usr/bin/python3
""" a class square that defines a square """


class Square:
    """ initializing a class with init """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size msut be >= 0")
        self.__size = size
    """ defining a square """
    def area(self):
        return self.__size * self.__size
