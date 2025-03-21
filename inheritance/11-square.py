#!/usr/bin/python3

"""Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
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
    

    def print(self):
        """Print the area of the rectangle"""
        print(self.__str__)


    def __str__(self):
        """Print the string representation"""
        return f"[Square] {self.__size}/{self.__size}"
    


if __name__ == "__main__":
    # Input Data
    s = Square(13)

    print(s)
    print(s.area())