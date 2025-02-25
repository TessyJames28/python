#!/usr/bin/python3

"""function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices:
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    