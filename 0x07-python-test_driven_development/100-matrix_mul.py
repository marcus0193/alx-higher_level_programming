#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Method that multiplies 2 matrices.

    Args:
        m_a: First matrix.
        m_b: second matrix.
    
    Return:
        matrix: The result

    Raises:
        TyprError: If m_a or m_b not list.
        TyprError: If m_a or m_b not list of lists.
        ValueError: If m_a or m_b are empty.
        TyprError: If m_a or m_b contain non int/float element.
        TyprError: If m_a or m_b not rectanqular.
        ValueError: If m_a or m_b can't multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must be of the same size")

    if m_a_notrect:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for i in range(len(m_a))]

    for n in range(len(m_a)):
        for y in range(len(m_b[0])):
            x = 0
            for m in range(len(m_b)):
                x += m_a[n][m] * m_b[m][y]
            res[n].append(x)

    return res

if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/100-matrix_mul.txt")
