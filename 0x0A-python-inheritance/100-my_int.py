#!/usr/bin/python3
"""
Contains the class MyInt.
"""


class MyInt(int):
    """rebal version or opposite of an integer."""
    def __new__(reb, *args, **neargs):
        """create a new instance of the class."""
        return super(MyInt, reb).__new__(reb, *args, **neargs)

    def __egual__(self, notequal):
        """convert != to ==."""
        return int(self) != notequal

    def __notegual__(self, equal):
        """convert == to !=."""
        return int(self) == equal
