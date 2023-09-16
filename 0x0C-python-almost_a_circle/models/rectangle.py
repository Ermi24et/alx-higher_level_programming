#!/usr/bin/python3
""" rectangle.py """
from .base import Base

class Rectangle(Base):
    """ a class rectangle that inherites from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of a rectangle.
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x coordinate of the rectangle
            y: y coordinate of the rectangle
            id: id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ gets height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ returns x coordinate of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the rectangle's x coordinate """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ returns y coordinate of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the rectangle's y coordiante """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ returns the area value of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with # """
        for i in range(self.__height):
                print("#" * self.__width)
