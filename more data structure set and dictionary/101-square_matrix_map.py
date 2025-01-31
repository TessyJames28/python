#!/usr/bin/python3

# function that computes the square value of all integers of a matrix using map

def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return new_matrix


# Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)