#!/usr/bin/python3
"""Defines from_json_string Method"""


import json


def from_json_string(my_str):
    """Returns string on json representation"""
    return json.loads(my_str)
