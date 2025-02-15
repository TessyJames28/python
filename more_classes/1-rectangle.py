#!/usr/bin/python3

# Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py


class Rectangle():
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height


    @property
    def width(self):
        # Getter method that retrieves the width
        return self.__width
    

    @width.setter
    def width(self, value):
        # Setter method for the width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        # Getter method to retrieve height
        return self.__height
    

    @height.setter
    def height(self, value):
        # Setter method to set the value of __height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


# Input Data
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)