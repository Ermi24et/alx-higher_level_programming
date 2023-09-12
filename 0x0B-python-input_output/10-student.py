#!/usr/bin/python3
""" defining a class student """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns description of a dictionary of an object """
        if attrs is None:
            return self.__dict__

        dict_list = {}

        for i in attrs:
            if hasattr(self, i):
                dict_list[i] = getattr(self, i)

        return dict_list
