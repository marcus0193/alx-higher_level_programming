#!/usr/bin/python3

"""
file contains the class State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class inherits from Base links to the MySQL table states
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state",
            cascade="all, delete-orphan"
            )

    def __str__(self):
        return self.name
