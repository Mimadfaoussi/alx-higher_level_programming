#!/usr/bin/python3
""" class definition of a City and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ City class that inherit from Base """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
