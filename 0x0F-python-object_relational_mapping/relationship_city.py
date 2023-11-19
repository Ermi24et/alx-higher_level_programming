#!/usr/bin/python3
"""
a script that contains the class definition of a city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    inherits from Base(imported from model_state)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
