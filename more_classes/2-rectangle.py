#!/usr/bin/python3

# Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)


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


    def area(self):
        # Returns area of a rectangle
        return self.width * self.height
    

    def perimeter(self):
        # Returns rectangle perimeter
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)
    


# Input Data
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))