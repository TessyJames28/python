#!/usr/bin/python3

"""Unittest for rectangle.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for rectangle.py"""

    def test_width(self):
        """test for width"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)

    def test_width_is_int(self):
        """test for width is int"""
        with self.assertRaises(TypeError) as context:
            Rectangle("2", 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_is_greater_than_0(self):
        """test for width is greater than 0"""
        with self.assertRaises(ValueError) as context:
            Rectangle(-10, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height(self):
        """test for height"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)

    def test_height_is_int(self):
        """test for height is int"""
        with self.assertRaises(TypeError) as context:
            Rectangle(2, "10")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_is_greater_than_0(self):
        """test for height is greater than 0"""
        with self.assertRaises(ValueError) as context:
            Rectangle(10, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x(self):
        """test for x"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.x, 0)

    def test_x_is_int(self):
        """test for x is int"""
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 10, "3")
        self.assertEqual(str(context.exception), "x must be an integer")
        
