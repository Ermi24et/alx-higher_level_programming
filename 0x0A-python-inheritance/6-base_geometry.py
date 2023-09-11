#!/usr/bin/python3
""" contains the BaseGeometry """


class BaseGeometry:
    """ a class that have a public attribute area """
    def area(self):
        """ rasies an exception when called """
        raise Exception("area() is not implementedi")
