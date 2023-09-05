#!/usr/bin/python3
""" unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest class for max_integer """
    def test_positive_nums(self):
        res = [23, 1, 45, 32, 99, 86]
        self.assertEqual(max_integer(res), 99)
    def test_negative_nums(self):
        res1 = [-23, -1, -45, -32, -99, -86]
        self.assertEqual(max_integer(res1), -1)
    def test_str_non(self):
        with self.assertRaises(TypeError):
            max_integer(['4', None, 4.34, 'w'])
    def test_empty(self):
        res2 = max_integer([])
        self.assertEqual(res2, None)
    def test_repeat_max(self):
        res3 = [9, 7, 6, 9]
        self.assertEqual(max_integer(res3), 9)
    def test_string_middle(self):
        res4 = [5, 3, "Hi", 7, 9]
        with self.assertRaises(TypeError):
            max_integer(res4)

if __name__ == "__main__":
    unittest.main()
