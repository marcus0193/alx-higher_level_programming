#!/usr/bin/python3

"""
file contains the class city and an instance Base = declarative_base():
inherits from Base (imported from model_state)
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class City(Base):
    """
    City class inherits from Base links to the MySQL table Cities
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")

    def __str__(self):
        return self.name
