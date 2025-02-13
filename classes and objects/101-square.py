#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 5-square.py)

class Square():
    def __init__(self, size = 0, position = (0, 0)):
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
        result = ""
        if square == 0:
            return f" "
        else:
            for i in range(square):
                result += (f"\n{pos[0] * ' '}{square * '#'}")
            return result


    def __str__(self):
        # String function to handle printing format for Square class
        try:
            return self.my_print()
        except TypeError:
            pass
    


# Input data
my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)