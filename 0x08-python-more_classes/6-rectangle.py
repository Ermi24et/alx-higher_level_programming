#!/usr/bin/python3
""" a rectangle class that defines a rectangle """


class Rectangle:
    """ define a rectangle class with width and height """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instaniation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ prints a string when an insatance deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        """ returns an area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns a perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ prints the '#' char of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        return ("\n".join(('#' * self.__width for i in range(self.__height))))

    def __repr__(self):
        """ returns a string representation """
        empt = ""

        if self.__width == 0 or self.__height == 0:
            return empt

        for i in range(self.__height):
            empt += ("#" * self.__width)

            if i < (self.__height - 1):
                empt += "\n"

        return empt
