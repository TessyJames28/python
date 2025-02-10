#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 4-square.py)

class Square():
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size # Private instance attribute

    
    def area(self):
        # returns the current square area
        return self.__size ** 2
    
    @property
    def size(self):
        # getter method that retrieves the size of the square
        return self.__size
    
    @size.setter
    def size(self, value):
        # setter method that sets the size of a square
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    
    def my_print(self):
        # Prints in stdout the square with the character '#'
        square = self.size
        if square == 0:
            print()
        else:
            for i in range(square):
                print(square * '#')


# Input Data
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")