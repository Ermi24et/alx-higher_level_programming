#!/usr/bin/python3
""" contains class Geometry and subclass rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ representation of a rectangle """
    def __init__(self, width, height):
        """ instationation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
