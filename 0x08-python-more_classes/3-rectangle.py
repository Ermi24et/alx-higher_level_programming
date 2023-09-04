#!/usr/bin/python3
""" Rectangle class that defines a rectangle """


class Rectangle:
    """ a class to test str and repr """
    def __init__(self, width=0, height=0):
        """ instationate """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getting width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting width """
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns an area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ prints the '#' character """
        if self.__width == 0 or self.height == 0:
            return ""
        return ("\n".join(('#' * self.__width for i in range(self.__height))))
