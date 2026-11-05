import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_digit = any(c in string.digits for c in pwd)
        has_symbol = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)

    def test_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_only_uppercase(self):
        pwd = generate_password(length=10, use_uppercase=True, use_lowercase=False, use_digits=False, use_symbols=False)
        self.assertEqual(len(pwd), 10)
        for c in pwd:
            self.assertTrue(c in string.ascii_uppercase)

    def test_only_digits(self):
        pwd = generate_password(length=8, use_uppercase=False, use_lowercase=False, use_digits=True, use_symbols=False)
        self.assertEqual(len(pwd), 8)
        for c in pwd:
            self.assertTrue(c in string.digits)

    def test_no_types_selected_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=False)

    def test_length_too_short_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=2) # Default wants 4 types, so length=2 is too short

if __name__ == '__main__':
    unittest.main()
