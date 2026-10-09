import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_contains_required_types_by_default(self):
        password = generate_password(length=20)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)

    def test_disable_uppercase(self):
        password = generate_password(length=20, use_uppercase=False)
        has_upper = any(c in string.ascii_uppercase for c in password)
        self.assertFalse(has_upper)

    def test_disable_numbers(self):
        password = generate_password(length=20, use_numbers=False)
        has_digit = any(c in string.digits for c in password)
        self.assertFalse(has_digit)

    def test_disable_symbols(self):
        password = generate_password(length=20, use_symbols=False)
        has_symbol = any(c in string.punctuation for c in password)
        self.assertFalse(has_symbol)

    def test_disable_all_but_lowercase(self):
        password = generate_password(length=20, use_uppercase=False, use_numbers=False, use_symbols=False)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)

        self.assertFalse(has_upper)
        self.assertFalse(has_digit)
        self.assertFalse(has_symbol)
        self.assertTrue(has_lower)

    def test_invalid_length_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_invalid_length_too_short_for_requirements(self):
        with self.assertRaises(ValueError):
            # Requires lower, upper, digit, symbol = 4 chars minimum. 3 is too short.
            generate_password(length=3, use_uppercase=True, use_numbers=True, use_symbols=True)

if __name__ == '__main__':
    unittest.main()
