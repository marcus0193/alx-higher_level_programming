#!/usr/bin/python3
"""Defines the class student"""


class Student:
    """Student representation."""
    def __init__(self, first_name, last_name, age):
        """Initializes the student record."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the student instance in dictionary representation."""
        return self.__dict__
