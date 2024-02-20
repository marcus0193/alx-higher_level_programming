#!/usr/bin/python3
"""Defines write_file Method"""


def write_file(filename="", text=""):
    """Reads filename from the two args usiing utf-8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
