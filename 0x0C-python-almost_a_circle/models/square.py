#!/usr/bin/python3
""" a Square class that inherites from rectangle """
from .rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string representation of a square """
        return '[Square] ({}) {}/{} - {}' \
                .format(self.id, self.x, self.y, self.width)

