#!/usr/bin/python3

"""function that multiplies 2 matrices using numpy library
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices using numpy:
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    else:
        # handle edge cases for matrix a
        for row in m_a:
            if not isinstance(row, list):
                raise TypeError("m_a must be a list of lists")
            elif len(row) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
            elif len(row) == 0:
                raise ValueError("m_a can't be empty")
            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("m_a should contain only integers or floats")
                
        # Handle edge cases for matrix b
        for row in m_b:
            if not isinstance(row, list):
                raise TypeError("m_b must be a list of lists")
            elif len(row) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
            elif len(row) == 0:
                raise ValueError("m_b can't be empty")
            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("m_b should contain only integers or floats")

    # last edge case with matrix multiplication algo
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)

        result = np.dot(matrix_a, matrix_b)
        return result
    

if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    print(lazy_matrix_mul([], [[1, 2], [3, 4]]))