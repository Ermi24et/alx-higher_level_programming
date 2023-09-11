#!/usr/bin/python3
"""
a module that contains the class MyList
"""


class MyList(list):
    """ subclass of a lsit """
    
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
