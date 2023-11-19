#!/usr/bin/python3
"""
a module that contains the class definition of a city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    inherits from Base(imported from model_state)
    attributes for the class:
        __table__(str): links to the MySQL table cities
        id(int): represents a column of an auto-generated, unique integer
        name(str): represents a column of a string of 128 characters
        state_id(int): represents a column of an integer, and is a foreign key
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
