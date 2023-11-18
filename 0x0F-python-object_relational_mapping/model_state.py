#!/usr/bin/python3

"""
a module that contains the class definition of a state and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    a class that inherits from Base(declarative base class)
    class attributes:
        __tablename__(str): a table mapped by the class State
        id(int): represents a column of an auto-generated, unique integer
        name(str): represents a column of a string with maximum 128 characters
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
