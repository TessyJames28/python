#!/usr/bin/python3

# Improve the BaseGeometry from 5-base_geometry.py

class BaseGeometry():
    """BaseGeometry class
    """

    def area(self):
        """Unimplemented area"""
        raise Exception("area() is not implemented")
    

# Input Data
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
