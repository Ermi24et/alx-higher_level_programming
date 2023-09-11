#!/usr/bin/python3
"""
a module that contains the class MyList
"""


class MyList(list):
    """ subclass of the list """
    def __init__(self):
        """initialization of the object"""
        super().__init__()
    
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
