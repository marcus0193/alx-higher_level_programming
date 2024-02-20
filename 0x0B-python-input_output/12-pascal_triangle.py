#!/usr/bin/python3
"""Module for pascal_triangle method"""


def pascal_triangle(n):
    """Method to represent pascal's trinagle of size n."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        t = triangle[-1]
        y = [1]
        for x in range(len(t) - 1):
            y.append(t[x] + t[x + 1])
        y.append(1)
        triangle.append(y)
    return triangle
