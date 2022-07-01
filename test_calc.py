import unittest
import unit_test

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = unit_test.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = unit_test.subract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = unit_test.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = unit_test.divide(10, 5)
        self.assertEqual(result, 2)
        with self.assertRaises(ValueError):
            unit_test.divide(10, 0)

if __name__ == '__main__':
    unittest.main()