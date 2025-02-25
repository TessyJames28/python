#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    num = [1,2,3,5,4,9,6,10,0]
    tuple_val = (1,2,3,5,4,9,6,10,0)
    def test_max(self):
        """Test for the maximum number
        """
        result = max_integer(self.num)
        self.assertTrue(result == 10)

    def test_none_max(self):
        """Test for none maximum value
        """
        result = max_integer(self.num)
        self.assertFalse(result == 9)

    def test_empty_list(self):
        """test for empty list
        """
        result = max_integer([])
        self.assertTrue(result == None)

    def test_tuple(self):
        """test for tuple
        """
        result = max_integer(self.tuple_val)
        self.assertTrue(result == 10)