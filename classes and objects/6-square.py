#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 5-square.py)

class Square():
    def __init__(self, size = 0, position = (0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size # Private instance attribute
        self.__position = position

    
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


    @property
    def position(self):
        # Getter method that retrieve the position
        return self.__position
    

    @position.setter
    def position(self, value):
        # Setter method that sets the value of position
        if not isinstance(value, tuple) and (value[0] and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
    
    def my_print(self):
        # Prints in stdout the square with the character '#'
        pos = self.position
        square = self.size
        if square == 0:
            print()
        else:
            for i in range(square):
                print(pos[0] * " ", square * '#')


# Input Data
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
