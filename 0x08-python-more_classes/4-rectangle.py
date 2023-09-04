#!/usr/bin/python3
""" a Rectangle class that defines a rectangle """


class Rectangle:
    """ a class that adds eval() to the previous task """
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
        """ getting height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns a perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ printing the char '#' """
        if self.__height == 0 or self.width == 0:
            return ""
        return ("\n".join(('#' * self.__width for i in range(self.__height))))

    def __repr__(self):
        """ enabling to recreate new instance using eval() """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
