#!/usr/bin/python3
"""Defines to_json_string Method"""


import json


def to_json_string(my_obj):
    """Returns object on json representation"""
    return json.dumps(my_obj)
