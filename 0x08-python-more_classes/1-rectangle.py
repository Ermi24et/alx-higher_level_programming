#!/usr/bin/python3
""" creating a rectangle class """


class Rectangle:
    """ defining a rectangle with private instances """
    def __init__(self, width=0, height=0):
        """ instatinating """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getting width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getting height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
