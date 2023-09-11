#!/usr/bin/python3
"""
a module that contains the lookup function
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
