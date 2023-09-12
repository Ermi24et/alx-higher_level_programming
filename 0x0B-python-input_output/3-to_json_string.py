#!/usr/bin/python3
""" contains the function JSON string """

import json


def to_json_string(my_obj):
    """ returns the json string representation of an object """
    return json.dumps(my_obj)
