#!/usr/bin/python3
"""
module for the rectangle class
"""
import unittest
import models.base as base
import models.rectangle as rec


class TestRectnagle(unittest.TestCase):
    """ test for the rectangle class """
    def test_module_doc(self):
        """ test for the module documentation """
        self.assertIsNotNone(rec.__doc__)
        self.assertGreater(len(rec.__doc__), 0)

    def test_class_doc(self):
        """ test for the class documentation """
        self.assertIsNotNone(rec.Rectangle.__doc__)
        self.assertGreater(len(rec.Rectangle.__doc__), 0)

    def test_init_met_doc(self):
        """ test for the instantiation documentation """
        self.assertIsNotNone(rec.Rectangle.__init__.__doc__)
        self.assertGreater(len(rec.Rectangle.__init__.__doc__), 0)

    def test_area_doc(self):
        """ test for the area method """
        self.assertIsNotNone(rec.Rectangle.area.__doc__)
        self.assertGreater(len(rec.Rectangle.area.__doc__), 0)

    def test_update_doc(self):
        """ test for the update method """
        self.assertIsNotNone(rec.Rectangle.update.__doc__)
        self.assertGreater(len(rec.Rectangle.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """ test for the to_dictionary method """
        self.assertIsNotNone(rec.Rectangle.to_dictionary.__doc__)
        self.assertGreater(len(rec.Rectangle.to_dictionary.__doc__), 0)

    def test_display_doc(self):
        """ test for the display documentation """
        self.assertIsNotNone(rec.Rectangle.display.__doc__)
        self.assertGreater(len(rec.Rectangle.display.__doc__), 0)

    def setup_test(self):
        """ resseting id """
        base.Base._Base__nb_objects = 0

    def test_rectangle_base(self):
        """ testing rectangle if it an instance of base """
        self.assertIsInstance(rec.Rectangle(3, 2), base.Base)

    def test_with_no_arg(self):
        """ testing rectnagle with no arg """
        with self.assertRaises(TypeError):
            rec.Rectangle()

    def test_with_more_args(self):
        """ testing with 1 and more than 1 arguments """
        r1 = rec.Rectangle(3, 2)
        r2 = rec.Rectangle(2, 3)
        r3 = rec.Rectangle(4, 4, 8)
        r4 = rec.Rectangle(8, 8, 4)
        r5 = rec.Rectangle(1, 2, 3, 4)
        r6 = rec.Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, r4.id - 1)
        self.assertEqual(r5.id, r6.id - 1)
        self.assertEqual(9, rec.Rectangle(3, 2, 0, 0, 9).id)

    def test_width_priv(self):
        """ tetsing access private width """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__width)

    def test_height_priv(self):
        """ tetsing access private height """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__height)

    def test_x_priv(self):
        """ testing access private x """
        with self.assertRaises(AttributeError):
            print(rec.rectangle(3, 3, 0, 0, 1).__x)

    def test_y_priv(self):
        """ testing access private y """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__y)

    def test_wid_none(self):
        """ tetsing width arg with none """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle(None, 3)

    def test_wid_str(self):
        """ tetsing width arg with string """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle("hello", 3)

    def test_wid_float(self):
        """ testing width arg with float """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle(3.3, 5)

    def test_wid_list(self):
        """ tetsing width arg with list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle([2, 3, 4], 3)

    def test_wid_dict(self):
        """ testing width arg with dictionary """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle({"b": 2, "c": 3}, 3)

    def test_wid_tuple(self):
        """ tetsting width arg with tuple """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle((2, 3, 4), 3)

    def test_heig_none(self):
        """ testing height arg with none """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(2, None)

    def test_heig_str(self):
        """ testing height arg with string """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(3, "hello")

    def test_heig_float(self):
        """ testing height arg with float """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(3, 4.5)

    def test_heig_list(self):
        """ testing height arg with list """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(3, [1, 2, 3])

    def test_heig_dict(self):
        """ testing height arg with dicttionary """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(3, {"b": 2, "c": 3})

    def test_heig_tuple(self):
        """ tetsing height arg with tuple """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(3, (2, 3, 4))

    def test_x_none(self):
        """ tetsing x arg with none """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, None)

    def test_x_str(self):
        """ testing x arg with string """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, "hello", 3)

    def test_x_float(self):
        """ testing x arg with float """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, 4.5, 7)

    def test_x_list(self):
        """ testing x arg with list """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, [2, 3, 4], 5)

    def test_x_dict(self):
        """ testing x arg with dictionary """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, {"b": 2, "c": 3}, 4)

    def test_x_tuple(self):
        """ tetsing x arg with tuple """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(2, 3, (2, 3, 4), 5)

    def test_y_none(self):
        """ testing y arg with none """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, None)

    def test_y_str(self):
        """ testing y arg with string """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, "hello")

    def test_y_float(self):
        """ testing y arg with float """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, 4.5)

    def tets_y_list(self):
        """ testing y arg with list """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, [2, 3, 4])

    def test_y_dict(self):
        """ testing y arg with dictionary """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, {"b": 2, "c": 3})

    def test_y_tuple(self):
        """ testing y arg with dictionary """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(2, 3, 4, (2, 3, 4))

    def test_area(self):
        """ tetsing area """
        r1 = rec.Rectangle(3, 10, 0, 0, 0)
        self.assertEqual(30, r1.area())

    def test_display(self):
        """ testing display """
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_update(self):
        """ testing update """
        r1 = rec.Rectangle(3, 4, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(78, "hello")

    def test_update_kwargs(self):
        """ testing update method kwargs """
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        r1.update(id=78, x=2, height=3)
        r1.update(y=5, height=23, width=3)
        self.assertEqual("[Rectangle] (78) 2/5 - 3/23", str(r1))

    def test_to_dictionary(self):
        """ tetsing dictionary method"""
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        r2 = rec.Rectangle(5, 3, 7, 4, 1)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
