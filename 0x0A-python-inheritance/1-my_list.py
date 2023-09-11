#!/usr/bin/python3
"""
holds a class MyList
"""


class MyList(list):
    """ a class that inherites from list """
    def print_sorted(self):
        """ prints an ordered list """
        print(sorted(self))
