#!/usr/bin/python3
""" Unit test for  HBNBCommand """

import unittest
import pycodestyle
from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime
import console


class TestHBNBCommand(unittest.TestCase):
    """ Test class HBNBCommand """
    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_prompt(self):
        """test the prompt format"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")


if __name__ == '__main__':
    unittest.main()
