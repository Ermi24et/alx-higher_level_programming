#!/usr/bin/python3
import dis
from math import pi


class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius
        def area(self):
            return self._MagicClass__radius ** 2 * pi


dis.dis(MagicClass)
