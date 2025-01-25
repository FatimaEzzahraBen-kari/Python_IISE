# tests/test_math_operations.py
import unittest
from src.math_operations import additionner, soustraire, multiplier, diviser

class TestMathOperations(unittest.TestCase):
    def test_additionner(self):
        self.assertEqual(additionner(2, 3), 5)
        self.assertEqual(additionner(-1, 1), 0)

    def test_soustraire(self):
        self.assertEqual(soustraire(5, 3), 2)
        self.assertEqual(soustraire(0, 5), -5)

    def test_multiplier(self):
        self.assertEqual(multiplier(4, 3), 12)
        self.assertEqual(multiplier(0, 5), 0)

    def test_diviser(self):
        self.assertEqual(diviser(6, 3), 2)
        with self.assertRaises(ValueError):
            diviser(5, 0)

if __name__ == "__main__":
    unittest.main()