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

    def test_x_is_greater_than_or_equal_to_0(self):
        """test for x is greater than or equal to 0"""
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, -3)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y(self):
        """test for y"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 3, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.y, 0)

    def test_y_is_int(self):
        """test for y is int"""
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 10, 3, "4")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_is_greater_than_or_equal_to_0(self):
        """test for y is greater than or equal to 0"""
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -4)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_id(self):
        """test for id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(2, 10)
        self.assertEqual(r2.id, 3)