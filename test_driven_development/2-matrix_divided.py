#!/usr/bin/python3

"""Write a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Returns a new matrix for the divided matrix"""
    
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        try:
            row_length = len(matrix[0])
        except TypeError:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for row in matrix:
            new_row = []
            if not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")
            else:
                for val in row:
                    if not isinstance(val, (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    else:
                        new_row.append(round(val/div, 2))
            new_matrix.append(new_row)
    
    return new_matrix
    

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, "3"))
    print(matrix)
