#!/usr/bin/python3

"""Unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for base.py"""

    @classmethod
    def setUp(cls):
        """Reset the Base class counter to 0"""
        Base._Base__nb_objects = 0

    def test_base(self):
        """test for the base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(6)
        self.assertEqual(b3.id, 6)

        b4 = Base()
        self.assertEqual(b4.id, 3)