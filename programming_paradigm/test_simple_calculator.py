import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(10, 5), 15)
        self.assertEqual(SimpleCalculator.add(-1, 1), 0)
        self.assertEqual(SimpleCalculator.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(10, 5), 5)
        self.assertEqual(SimpleCalculator.subtract(-1, 1), -2)
        self.assertEqual(SimpleCalculator.add(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(10, 5), 50)
        self.assertEqual(SimpleCalculator.multiply(-1, 1), -1)
        self.assertEqual(SimpleCalculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(10, 5), 2)
        self.assertEqual(SimpleCalculator.divide(-1, 1), -1)
        self.assertEqual(SimpleCalculator.divide(-1, -1), 1)

        self.assertRaises(ValueError, SimpleCalculator.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()



