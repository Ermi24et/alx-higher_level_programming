#!/usr/bin/python3
""" a function that reads a text file """


def read_file(filename=""):
    """ a function that reads a text file prints """
    with open(filename, mode="r", encoding='utf-8') as f:
        print(f.read(), end="")
