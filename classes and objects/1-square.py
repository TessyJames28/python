#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 0-square.py)

class Square():
    def __init__(self, size):
        self.__size = size # Private instance attribute


# Input data
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
