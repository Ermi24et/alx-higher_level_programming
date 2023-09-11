#!/usr/bin/python3
""" contains is_same class """


def is_same_class(obj, a_class):
    """return true if the function is exactly an instance of the class"""
    return (type(obj) == a_class)
