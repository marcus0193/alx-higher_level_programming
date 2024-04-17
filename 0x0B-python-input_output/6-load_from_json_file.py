#!/usr/bin/python3
"""Defines load_from_json_file Method"""


import json


def load_from_json_file(filename):
    """Creates an object from file on json representation"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
