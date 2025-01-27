#!/usr/bin/python3

# function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    squared_element = lambda num: num ** 2
    new_matrix = [[squared_element(val) for val in row] for row in matrix]
    return new_matrix
    


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)