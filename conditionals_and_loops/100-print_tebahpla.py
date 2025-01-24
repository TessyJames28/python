#!/usr/bin/python3

for val in range(90, 64, -1):
    if val % 2 == 0:
        val += 32
    print(chr(val), end="")