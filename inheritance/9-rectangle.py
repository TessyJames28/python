#!/usr/bin/python3

""" Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry and use interger_validator 
    to validate height and width
    """
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height


    def area(self):
        """Return the area of a Rectangle"""
        return self.__height * self.__width
    

    def print(self):
        """Print the area of the rectangle"""
        print(self.__str__)


    def __str__(self):
        """Print the string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

# Input data
r = Rectangle(3, 5)

print(r)
print(r.area())
