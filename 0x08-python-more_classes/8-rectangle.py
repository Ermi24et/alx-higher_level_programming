#!/usr/bin/python3
""" a rectangle class that defines a rectangle """


class Rectangle:
    """ class that adds static method to prev function """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """ Instantionate """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ prints a string when an instance deleted """
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
        """ returns area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns printable string representation of rectangle """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """ returns a string representation of rectangle for reproduction """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
