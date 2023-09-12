#!/usr/bin/python3
"""a function that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """ returns the number of characters added """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
