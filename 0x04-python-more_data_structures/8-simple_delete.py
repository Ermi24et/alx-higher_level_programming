#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    res = str(key)
    if res in a_dictionary:
        a_dictionary.pop(res)
    return a_dictionary
