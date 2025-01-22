import unittest
from module_exceptions import (
    safe_division,
    convert_to_int,
    read_file,
    NegativeAgeError,
    set_age,
    process_input
)

class TestExceptions(unittest.TestCase):
    
    def test_safe_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

    def test_safe_division_normal(self):
        self.assertEqual(safe_division(10, 2), 5)  # Test d'une division normale

    def test_convert_to_int_invalid(self):
        with self.assertRaises(ValueError):
            convert_to_int("abc")

    def test_convert_to_int_valid(self):
        self.assertEqual(convert_to_int("123"), 123)  # Test avec une valeur valide

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")
            
    def test_set_age_negative(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-1)

    def test_set_age_positive(self):
        self.assertEqual(set_age(25), 25)  # Test avec un âge valide

    def test_process_input_invalid(self):
        with self.assertRaises(ValueError):
            process_input("abc")

    def test_process_input_valid(self):
        self.assertEqual(process_input("42"), 42)  # Test avec une entrée valide

if __name__ == '__main__':
    unittest.main()
