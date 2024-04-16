#!/usr/bin/python3
"""
Contains the class MyInt.
"""


class MyInt(int):
    """rebal version or opposite of an integer."""
    def __new__(reb, *args, **neargs):
        """create a new instance of the class."""
        return super(MyInt, reb).__new__(reb, *args, **neargs)

    def __eq__(self, note):
        """convert != to ==."""
        return int(self) != note

    def __ne__(self, e):
        """convert == to !=."""
        return int(self) == e
