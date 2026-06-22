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

    def test_includes_uppercase(self):
        password = generate_password(include_uppercase=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

    def test_excludes_uppercase(self):
        password = generate_password(include_uppercase=False, length=100)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_includes_numbers(self):
        password = generate_password(include_numbers=True)
        self.assertTrue(any(c in string.digits for c in password))

    def test_excludes_numbers(self):
        password = generate_password(include_numbers=False, length=100)
        self.assertFalse(any(c in string.digits for c in password))

    def test_includes_symbols(self):
        password = generate_password(include_symbols=True)
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        self.assertTrue(any(c in symbols for c in password))

    def test_excludes_symbols(self):
        password = generate_password(include_symbols=False, length=100)
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        self.assertFalse(any(c in symbols for c in password))

    def test_all_excluded(self):
        # Only lowercase should remain
        password = generate_password(include_uppercase=False, include_numbers=False, include_symbols=False, length=50)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_length_too_short_for_constraints(self):
        # Requires 4 chars (lowercase, uppercase, numbers, symbols)
        with self.assertRaises(ValueError):
            generate_password(length=3, include_uppercase=True, include_numbers=True, include_symbols=True)

        # Requires 2 chars (lowercase, numbers)
        with self.assertRaises(ValueError):
            generate_password(length=1, include_uppercase=False, include_numbers=True, include_symbols=False)

if __name__ == '__main__':
    unittest.main()
