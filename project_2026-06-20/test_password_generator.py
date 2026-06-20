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

    def test_length_less_than_pool_size(self):
        password = generate_password(length=2)
        self.assertEqual(len(password), 2)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_no_character_pools(self):
        with self.assertRaises(ValueError):
            generate_password(include_uppercase=False, include_lowercase=False, include_digits=False, include_symbols=False)

    def test_only_uppercase(self):
        password = generate_password(include_lowercase=False, include_digits=False, include_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_only_lowercase(self):
        password = generate_password(include_uppercase=False, include_digits=False, include_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_only_digits(self):
        password = generate_password(include_uppercase=False, include_lowercase=False, include_symbols=False)
        for char in password:
            self.assertIn(char, string.digits)

    def test_only_symbols(self):
        password = generate_password(include_uppercase=False, include_lowercase=False, include_digits=False)
        for char in password:
            self.assertIn(char, string.punctuation)

    def test_contains_all_requested(self):
        password = generate_password(length=4, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)

if __name__ == '__main__':
    unittest.main()
