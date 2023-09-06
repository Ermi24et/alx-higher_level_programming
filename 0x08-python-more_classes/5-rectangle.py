#!/usr/bin/python3
""" a rectangle class that defines a rectangle """


class Rectangle:
    """ a class that adds public class attribute to the prev """
    def __init__(self, width=0, height=0):
        """ instanition """
        self.width = width
        self.height = height

    def __del__(self):
        """ prints a string when an instance deleted """
        print("Bye rectangle...")

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
        """ returns the area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns teh perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ prints the rectangle with the char '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(('#' * self.__width for i in range(self.__height))))

    def __repr__(self):
        """ returns a string to recreate new instance by using eval() """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
