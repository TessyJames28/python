#!/usr/bin/python3
# A program that prints the ASCII alphabets, in lowercase
# not followed by a new line.
for letter in range(97, 123):
    if chr(letter) == "q" or chr(letter) == "e":
        continue
    print(f"{chr(letter)}", end="")