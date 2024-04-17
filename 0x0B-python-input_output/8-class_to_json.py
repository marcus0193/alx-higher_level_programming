#!/usr/bin/python3
"""Defines class_to_json Method"""


def class_to_json(obj):
    """Returns a json serialization of an object
    with simple dictionary description"""
    return obj.__dict__
