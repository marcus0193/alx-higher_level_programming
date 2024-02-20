#!/usr/bin/python3
"""Defines append_write Method"""


def append_write(filename="", text=""):
    """Append filename from the two args usiing utf-8"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
