#!/usr/bin/python3

"""Write a class Square that inherits from Rectangle (9-rectangle.py):
"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Class Square Inherits from Rectangle
    """
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    
    def area(self):
        """Area of a Square"""
        return self.__size ** 2
    

if __name__ == "__main__":
    # Input Data
    s = Square(13)

    print(s)
    print(s.area())