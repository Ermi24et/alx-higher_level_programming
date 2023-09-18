#!/usr/bin/python3
"""
unittest module for the Base class
"""
import unittest
import models.base as base


class TestBase(unittest.TestCase):
    """
    a class TestBase
    """
    def test_module_doc(self):
        """ test for the module documentation """
        self.assertIsNotNone(base.__doc__)
        self.assertGreater(len(base.__doc__), 0)

    def test_class_doc(self):
        """ test for the class documentation """
        self.assertIsNotNone(base.Base.__doc__)
        self.assertGreater(len(base.Base.__doc__), 0)

    def test_method_doc(self):
        """ test for the method documentation """
        self.assertIsNotNone(base.Base.__init__.__doc__)
        self.assertGreater(len(base.Base.__init__.__doc__), 0)

    def test_to_json_string_doc(self):
        """ test for the static method documentation """
        self.assertIsNotNone(base.Base.to_json_string.__doc__)
        self.assertGreater(len(base.Base.to_json_string.__doc__), 0)

    def setup_test_case(self):
        """ set up the test case by reseting the __nb_objects to 0 """
        base.Base._Base__nb_objects = 0

    def test_id_if_none(self):
        """ test if id is none """
        i1 = base.Base(None)
        i2 = base.Base()
        self.assertEqual(i1.id, i2.id - 1)

    def test_id_for_incr(self):
        """ test for id if incremented by 1 """
        i1 = base.Base()
        i2 = base.Base()
        self.assertEqual(i1.id, i2.id - 1)

    def test_for_args(self):
        """ test for id more than 1 """
        with self.assertRaises(TypeError):
            base.Base(3, 8)

    def test_for_bool(self):
        """ test for boolean value """
        self.assertEqual(base.Base(True).id, True)

    def test_for_str(self):
        """ test for strings """
        self.assertEqual(base.Base("hello").id, "hello")

    def test_private_attr(self):
        """ test for accessing private attribute """
        with self.assertRaises(AttributeError):
            base.Base(5).__nb_objects


class TestBase_to_json_string(unittest.TestCase):
    """ test for the to_json_string method """
    def test_to_json_string_emp(self):
        """ test to_json_string with empty list """
        emp_str = base.Base.to_json_string([])
        self.assertIsInstance(emp_str, str)
        self.assertEqual(emp_str, "[]")

    def test_to_json_str_no_args(self):
        """ test for to_json_string with out an argument """
        with self.assertRaises(TypeError):
            base.Base.to_json_string()

    def test_to_json_string_none(self):
        """ test to to_json_string with none """
        self.assertEqual(base.Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        """ test to to_json_string with more than 1 args """
        with self.assertRaises(TypeError):
            base.Base.to_json_string([], 5)


class TestBase_from_json_string(unittest.TestCase):
    """ test for the from_json_string to the method"""
    def test_from_json_string_none(self):
        """ test from_json_string with none """
        self.assertEqual(base.Base.from_json_string(None), [])

    def test_from_json_string_args(self):
        """ test from_json_string with more than 1 args """
        with self.assertRaises(TypeError):
            base.Base.from_json_string([], 5)

    def test_from_json_string_no_args(self):
        """ test from_json_string with no args to method"""
        with self.assertRaises(TypeError):
            base.Base.from_json_string()


if __name__ == "__main__":
    unittest.main()
