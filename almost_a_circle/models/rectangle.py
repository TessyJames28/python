#!/usr/bin/python3
from models.base import Base

"""Write the class Rectangle that inherits from Base:
"""

class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """x setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


    def area(self):
        """Return the area of the rectangle
        """
        return self.width * self.height
    

    def display(self):
        """print the rectangle with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("#" * self.__width)


    def __str__(self):
        """Overide __str__ represtentation to print a new string format
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute based on key/value pairs:
        """
        for key, val in kwargs.items():
            if key == "id":
                self.id = val
            elif key == "width":
                self.__width = val
            elif key == "height":
                self.__height = val
            elif key == "x":
                self.__x = val
            elif key == "y":
                self.__y = val
                
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]