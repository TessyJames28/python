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

    jump = 1
    cols = []
    

    for row in range(arg):
        rows = []
        print(f"first jump: {jump}")
        for col in range(1, arg - 1):
            if row == 0:
                rows.append([row, col])
            else:
                if (col + jump) >= (arg - 1):
                    new_jump = (col + jump) % (arg - 1)
                    print(jump)
                    rows.append([row, new_jump])
                else:
                    rows.append([row, col + jump])
            cols.append(rows)
        if row == 0:
            jump += 2
        
    return cols


print(nqueens(4))


def transpose(matrix):
    return[[row[i] for row in matrix] for i in range(len(matrix[0]))]


        