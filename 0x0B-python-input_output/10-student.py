#!/usr/bin/python3
"""Module to defines the class student"""


class Student:
    """Student representation."""
    def __init__(self, first_name, last_name, age):
        """Initializes the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the student instance in dictionary representation
        with only the listed attributes."""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
