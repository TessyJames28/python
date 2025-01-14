#!/usr/bin/python3
# Write a program that prints all possible
# different combinations of two digits.

for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            continue
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")