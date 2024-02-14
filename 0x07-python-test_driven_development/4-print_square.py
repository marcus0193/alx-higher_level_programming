#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Method that prints a square with the character #.


    Args:
        size: The size of the square in int.

    Raises:
        TypeError: If size not int.
        ValueError: If size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
