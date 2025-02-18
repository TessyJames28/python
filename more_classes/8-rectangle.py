#!/usr/bin/python3

# Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)


class Rectangle():
    number_of_instances = 0 # number_of_instances the instances created
    print_symbol = '#' # Used as symbol for string representation

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1 # Increment the number_of_instances when an instance is created


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
        

    def print(self):
        # print rectangle with the charater '#'
        result = ""
        for i in range(self.height):
            if i == self.height - 1:
                result += f"{self.print_symbol * self.width}"
            else:
                result += f"{self.print_symbol * self.width}\n"
        return result
    

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # Returns the biggest rectangle based on the area
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
    

    def __gt__(self, obj):
        if isinstance(obj, Rectangle):
            return self.area() > self.area()
       

    def __str__(self):
        # Return the print method format for rectangle
        return self.print()
    

    def __repr__(self):
        # Returns a string representation of the Rectangle
        value = f"Rectangle({self.__width}, {self.__height})"
        return value
    

    def __del__(self):
        # Define cleanup action
        Rectangle.number_of_instances -= 1 # Decrement the number_of_instances when an instance is deleted
        print("Bye rectangle...")


# Input Data
my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")