#!/usr/bin/python3

"""
Module for lazy_matrix_mul method using numpy module.
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Method to multiplies 2 matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        m_a * m_b
    """

    return numpy.matmul(m_a, m_b)
