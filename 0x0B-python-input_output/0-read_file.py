#!/usr/bin/python3
"""Defines read_file Method"""


def read_file(filename=""):
    """Reads filename using utf-8 encoding"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
