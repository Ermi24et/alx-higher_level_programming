#!/usr/bin/python3
""" contains the class BaseGeometry """


class BaseGeometry:
    """a class with instance methods in area and integer_validator"""
    def area(self):
        """ raises an exception when called """
        raise Exception("area() is not implemnted")

    def integer_validator(self, name, value):
        """ validates that value is an integer greater than zero"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
