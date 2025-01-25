#!/usr/bin/python3

# Function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("")
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()