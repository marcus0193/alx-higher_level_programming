#!/usr/bin/python3
"""Defines save_to_json_file Method"""


import json


def save_to_json_file(my_obj, filename):
    """Writes and object to file on json representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
