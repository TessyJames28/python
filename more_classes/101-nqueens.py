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
    cols = []
    column = []  

    for row in range(arg):
        rows = []
        val = 0
        for col in range(1, arg - 1):
            if row == 0:
                rows.append(f"{[row, col]}")
            else:
                if col == 1:
                    val = row + jump
                    if val > arg:
                        val = (val - arg) - 1
                        rows.append(f"{[row, val]}")
                    else:
                        rows.append(f"{[row, val]}")
                else:
                    val += jump
                    if val > arg:
                        val = (val - arg) - 1
                        rows.append(f"{[row, val]}")
                    else:
                        rows.append(f"{[row, val]}")
        
        #Handle the jump
        if row >= 1:
            jump += 1
        column.append(rows) # Append to a temporary list

    # Format the out
    for lst in column:
        formated_row = ", ".join(f"{pos}" for pos in lst)
        cols.append(f"[{formated_row}]")
        
        
    return "\n".join(cols)
        

# nqueens(6)

# Handle the transposing of the list
def transpose(matrix):
    return[[row[i] for row in matrix] for i in range(len(matrix[0]))]


matrix = nqueens(6)
print(transpose(matrix))
        