#!/usr/bin/python3
""" contains the function that returns an object """

import json


def from_json_string(my_str):
    """ returns an object represented by JSON string """
    return json.loads(my_str)
