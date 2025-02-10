#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 2-square.py)

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



# input data
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)