#!/usr/bin/python3
""" a script that adds all arguments to a python list """

from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    list_of_json = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_of_json = []

for arg in argv[1:]:
    list_of_json.append(arg)

save_to_json_file(list_of_json, "add_item.json")
