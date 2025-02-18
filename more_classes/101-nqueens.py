#!/usr/bin/python3
import sys

# The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
# Write a program that solves the N queens problem.
# Usage: nqueens N
def nqueens(arg):
    # num_args = len(arg)
    # if num_args > 2:
    #     print("Usage: nqueens N")
    #     exit(1)
    # elif not isinstance(num_args[1], int):
    #     print("N must be a number")
    #     exit(1)
    # elif num_args[1] < 4:
    #     print("N must be at least 4")
    #     exit(1)

    jump = 2    

    for row in range(arg):
        rows = []
        val = 0
        for col in range(1, arg - 1):
            if row == 0:
                rows.append([row, col])
            else:
                if col == 1:
                    val = row + jump
                    if val > arg:
                        val = (val - arg) - 1
                        rows.append([row, val])
                    else:
                        rows.append([row, val])
                else:
                    val += jump
                    if val > arg:
                        val = (val - arg) - 1
                        rows.append([row, val])
                    else:
                        rows.append([row, val])
            
        if row >= 1:
            jump += 1
        print(rows)
        


nqueens(6)


def transpose(matrix):
    return[[row[i] for row in matrix] for i in range(len(matrix[0]))]


        