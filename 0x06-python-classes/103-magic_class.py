#!/usr/bin/python3
""" defines a magic class """
import math


class MagicClass:
    """ magic class """
    def __init__(self, radius=0):
        """ initialization of init """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """ calculates area """
            return (self.__radius ** 2) * math.pi

        def circumference(self):
            """ circumference of a circle """
            return 2 * math.pi * self.__radius
