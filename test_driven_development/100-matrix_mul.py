#!/usr/bin/python3

"""function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices:
    """
    try:
        row_length = len(m_a[0])
    except Exception:
        raise TypeError("m_a can't be empty")
    
    try:
        row_length = len(m_b[0])
    except Exception:
        raise TypeError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    else:
        for row in m_a:
            if not isinstance(row, list):
                raise TypeError("m_a must be a list of lists")
            elif len(row) != row_length:
                raise TypeError("each row of m_a must be of the same size")
            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("m_a should contain only integers or floats")
                
    
        for row in m_b:
            if not isinstance(row, list):
                raise TypeError("m_b must be a list of lists")
            elif len(row) != row_length:
                raise TypeError("each row of m_b must be of the same size")
            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        matrix = []
        cols = len(m_a[0]) 
        try:         
            for col in range(cols):
                new_row = []
                for row in range(len(m_b[0])):
                    
                    result = 0
                    for val in range(len(m_b)):
                        result += (m_a[col][val] * m_b[val][row])
                    new_row.append(result)
            
                matrix.append(new_row)
        except Exception:
            pass
        return matrix

if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    print(matrix_mul([[1, 2], [3, 4]], [[1,2]]))

