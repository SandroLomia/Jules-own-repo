import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=32)
        self.assertEqual(len(password), 32)

    def test_only_uppercase(self):
        password = generate_password(length=50, use_lower=False, use_digits=False, use_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_only_lowercase(self):
        password = generate_password(length=50, use_upper=False, use_digits=False, use_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_only_digits(self):
        password = generate_password(length=50, use_upper=False, use_lower=False, use_symbols=False)
        for char in password:
            self.assertIn(char, string.digits)

    def test_only_symbols(self):
        password = generate_password(length=50, use_upper=False, use_lower=False, use_digits=False)
        for char in password:
            self.assertIn(char, string.punctuation)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

if __name__ == "__main__":
    unittest.main()
