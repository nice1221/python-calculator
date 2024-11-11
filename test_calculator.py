import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    # Add the following test methods to the TestCalculator class:

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(1, 1), 1)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(1, -1), -1)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(1, 0), "Cannot divide by Zero.")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(15, 4), 3)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(11, -2), -1)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(1, 0), "Cannot mod by Zero.")

if __name__ == '__main__':
    unittest.main()
