#!/usr/bin/python3
import sys

# The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
# Write a program that solves the N queens problem.
# Usage: nqueens N
def nqueens():
    if len(sys.argv) > 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
        
    if arg < 4:
        print("N must be at least 4")
        exit(1)

    jump = 2  
    cols = []

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
        cols.append(rows) # Append to a temporary list
        
        #Handle the jump
        if row >= 1:
            jump += 1
        
    return cols
   


# Handle the transposing of the list
def transpose(matrix):
    # Fyunction to transpose the matrix for nqueens calculation
    transpose = []
    cols = len(matrix[0])
    rows = len(matrix)
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transpose.append(new_row)
    return transpose


matrix = nqueens()
result = transpose(matrix)
for row in result:
    print(row)
        