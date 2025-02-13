#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 4-square.py)
# Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area

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
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    
    # Defining special methods (dunder methods) to support square class comparison
    def __eq__(self, obj):
        # Equality comparison
        if isinstance(obj, Square):
            return self.area() == obj.area()
        

    def __ne__(self, obj):
        # Not Equal comparison
        if isinstance(obj, Square):
            return self.area() != obj.area()
        

    def __gt__(self, obj):
        # Greater than comparison
        if isinstance(obj, Square):
            return self.area() > obj.area()
        

    def __lt__(self, obj):
        # Less than comparison
        if isinstance(obj, Square):
            return self.area() < obj.area()
        

    def __le__(self, obj):
        # Less than or equal to comparison
        if isinstance(obj, Square):
            return self.area() <= obj.area()
        

    def __ge__(self, obj):
        # Greater than or equal to comparison
        if isinstance(obj, Square):
            return self.area() >= obj.area()
        
        
        
    


# Input Data
s_5 = Square(5)
s_6 = Square(6)
print(s_5, s_6)

if s_5 < s_6:
    print("Square 5 < Square 6")
else:
    print("Square 5 not < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")