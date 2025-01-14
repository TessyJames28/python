#!/usr/bin/python3
def print_last_digit(number):
    return abs(number) % 10


print(print_last_digit(98), end="")
print(print_last_digit(0), end="")
r = print_last_digit(-1024)
print(print_last_digit(-1024), end="")
print(r)