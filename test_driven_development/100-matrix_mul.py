#!/usr/bin/python3

"""function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices:
    """
    cols = m_a[0]
    rows = m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif not isinstance(rows, list):
        raise TypeError("m_a must be a list of lists")
    elif not isinstance(m_a, (int, float)):
        raise TypeError("m_a should contain only integers or floats")
    elif not isinstance()
    else:
        for col in range(cols):
            for row in range(rows)

    print(f"rows: {rows}")
    print(f"cols{cols}")

matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
matrix_mul([[1, 2]], [[3, 4], [5, 6]])

    