#!/usr/bin/python3
# A program that prints the ASCII alphabets, in lowercase
# not followed by a new line.
for letters in range(97, 123):
    print(f"{chr(letters)}", end="")