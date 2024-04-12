#!/usr/bin/python3
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
    
    def test_float_numbers(self):
        """Test list with floating-point numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3]), -1.1)

    def test_mixed_numbers(self):
        """Test list with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)
        self.assertEqual(max_integer([-1.1, -2, -3.3]), -1.1)
    
    def test_single_element_list(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)
    
    def test_duplicate_numbers(self):
        """Test list with duplicate numbers"""
        self.assertEqual(max_integer([7, 7, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_large_numbers(self):
        """Test list with large numbers"""
        self.assertEqual(max_integer([999999999999, 1000000000000, 9999999999999]), 9999999999999)
        self.assertEqual(max_integer([-999999999999, -1000000000000, -9999999999999]), -999999999999

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name") 

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
