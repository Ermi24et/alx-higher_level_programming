#!/usr/bin/python3
""" contains a function that writes an object to text file """

import json


def save_to_json_file(my_obj, filename):
    """ a funtion that writes an object to a text file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
