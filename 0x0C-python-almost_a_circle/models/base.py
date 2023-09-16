#!/usr/bin/python3
""" base.py """
import json


class Base:
    """
    the base class of all classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of lists_objs to a file
        """
        filename = cls.__name__ + ".json"
        j_list = [o.to_dictionary() for o in list_objs]
        j_str = cls.to_json_string(j_list)

        with open(filename, "w") as f:
            f.write(j_str)
