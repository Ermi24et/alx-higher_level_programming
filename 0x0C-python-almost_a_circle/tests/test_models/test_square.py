#!/usr/bin/python3
""" module for the unittest of the class Square """
import unittest
import models.square as sq
import models.base as base


class TestSquare(unittest.TestCase):
    """ test for the class Square """
    def test_module_doc(self):
        """ test module documentation """
        self.assertIsNotNone(sq.__doc__)
        self.assertGreater(len(sq.__doc__), 0)

    def test_class_doc(self):
        """ test class documentation """
        self.assertIsNotNone(sq.Square.__doc__)
        self.assertGreater(len(sq.Square.__doc__), 0)

    def test_init_doc(self):
        """ test instantiation documentation """
        self.assertIsNotNone(sq.Square.__init__.__doc__)
        self.assertGreater(len(sq.Square.__init__.__doc__), 0)

    def test_update_doc(self):
        """ test for the update documentation """
        self.assertIsNotNone(sq.Square.update.__doc__)
        self.assertGreater(len(sq.Square.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """ test for the to_dictionary documentation """
        self.assertIsNotNone(sq.Square.to_dictionary.__doc__)
        self.assertGreater(len(sq.Square.to_dictionary.__doc__), 0)

    def test_square_base(self):
        """ test square is an instance of base """
        self.assertIsInstance(sq.Square(20), base.Base)

    def test_square_with_no_arg(self):
        """ test square with no argumnets """
        with self.assertRaises(TypeError):
            sq.Square()

    def test_1_arg(self):
        """ test square with one argumnet """
        s1 = sq.Square(20)
        s2 = sq.Square(21)
        self.assertEqual(s1.id, s2.id - 1)

    def test_2_args(self):
        """ test square with two arguments """
        s1 = sq.Square(20, 4)
        s2 = sq.Square(4, 20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_3_args(self):
        """ test square with three arguments """
        s1 = sq.Square(20, 4, 4)
        s2 = sq.Square(4, 4, 20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_4_args(self):
        """ test square with 4 arguments """
        self.assertEqual(9, sq.Square(20, 4, 4, 9).id)

    def test_more_than_4(self):
        """ test sqaure with more than 4 arguments """
        with self.assertRaises(TypeError):
            sq.Square(2, 3, 4, 5, 6)

    def test_size_priv_attr(self):
        """ test to access private attribute of size """
        with self.assertRaises(AttributeError):
            print(sq.Square(3, 5, 7, 9).__size)

    def test_size_none(self):
        """ test size with none """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square(None)

    def test_size_str(self):
        """ test size with string """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square("hello")

    def test_size_float(self):
        """ test size with float """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square(6.3)

    def tets_size_list(self):
        """ test size with list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square([2, 3, 4])

    def test_x_none(self):
        """ test x with none """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(2, None)

    def test_x_str(self):
        """ test x with string """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(2, "hello")

    def test_x_float(self):
        """ test x with float """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(2, 3.7)

    def test_x_list(self):
        """ test x with list """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(2, [2, 3, 4])

    def test_y_none(self):
        """ test y with none """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(2, 3, None)

    def test_y_str(self):
        """ test y with strings """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(2, 3, "hello")

    def test_y_float(self):
        """ test y with float """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(2, 3, 3.5)

    def test_y_list(self):
        """ test y with list """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(2, 3, [1, 2, 3])

    def test_area(self):
        """ test for an area """
        self.assertEqual(9, sq.Square(3, 0, 0, 1).area())

    def test_str_method(self):
        """ test for a str method for changed attributes """
        s1 = sq.Square(7, 0, 0, [4])
        s1.size = 23
        s1.x = 7
        s1.y = 20
        self.assertEqual("[Square] ([4]) 7/20 - 23", str(s1))

    def test_update_args(self):
        """ test update args method of square class """
        s1 = sq.Square(20, 30, 40, 50)
        s1.update(78, 5, 7, 9)
        self.assertEqual("[Square] (78) 7/9 - 5", str(s1))

    def test_update_arg(self):
        """ test update args method of sqaure class """
        s1 = sq.Square(20, 30, 40, 50)
        s1.update(78, 3, 4, 5)
        s1.update(5, 4, 3, 78)
        self.assertEqual("[Square] (5) 3/78 - 4", str(s1))

    def test_update_kwargs(self):
        """ test update kwargs method of square class """
        s1 = sq.Square(20, 30, 40, 50)
        s1.update(id=78, x=1)
        s1.update(y=4, x=24, size=2)
        self.assertEqual("[Square] (78) 24/4 - 2", str(s1))

    def test_to_dictionary_op(self):
        """ test to_dictionary method of sqaure class """
        s1 = sq.Square(20, 3, 1, 1)
        res = {'id': 1, 'x': 3, 'size': 20, 'y': 1}
        self.assertDictEqual(res, s1.to_dictionary())


if __name__ == "__main__":
    unittest.main()
