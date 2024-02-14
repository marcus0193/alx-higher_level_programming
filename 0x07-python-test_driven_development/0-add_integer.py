#!/usr/bin/python3
"""Module for the add_integer method."""


def add_integer(a, b=98):
    """Sum the two given args.


    Args:
        a: the fisrt arg.
        b: the sec arg.

    Raises:
        TypeError: if the two args are not int or float.

    Returns:
        the sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
