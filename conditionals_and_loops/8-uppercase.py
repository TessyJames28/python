#!/usr/bin/python3
# Write a function that prints a string in uppercase followed by a new line.
def uppercase(str):
    cap_str = ""
    for char in str:
        if ord(char) in range(65, 91) or ord(char) not in range(97, 123):
            cap_str += char
        else:
            cap_str += chr((ord(char) - 32))
    print(cap_str)


uppercase("best")
uppercase("Best School 98 Battery street")