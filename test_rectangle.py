import unittest
import rectangle

class rectangle_test_case(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(rectangle.area(5, 3), 15)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_negative(self):
        self.assertEqual(rectangle.area(-4, 5), -20)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(5, 3), 16)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_perimeter_negative(self):
        self.assertEqual(rectangle.perimeter(-4, 5), 2)

if __name__ == '__main__':
    unittest.main()
