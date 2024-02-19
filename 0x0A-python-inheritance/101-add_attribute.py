#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, atr, value):
    """Adds a new attribute to an object.

    Args:
        obj (any): the object to add to.
        atr (str): the name of the added attribute.
        value (any): the value of the attribute.

    Raises:
        TypeErroe: if the attribute not compatible with the obj.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
