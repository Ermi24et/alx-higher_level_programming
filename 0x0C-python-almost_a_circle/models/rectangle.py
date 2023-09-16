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
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ it returns the rectangle's id, x, y, height, width """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        args_l = ["id", "width", "height", "x", "y"]
        args_len = len(args_l)
        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < args_len:
                    self.__setattr__(args_l[i], argv)
        else:
            for e, f in kwargs.items():
                self.__setattr__(e, f)

    def to_dictionary(self):
        """ returns the dictionary representation of a rectangle """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
