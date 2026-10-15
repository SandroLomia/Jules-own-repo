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

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_only_lowercase(self):
        password = generate_password(length=100, use_uppercase=False, use_numbers=False, use_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_only_uppercase(self):
        password = generate_password(length=100, use_lowercase=False, use_uppercase=True, use_numbers=False, use_symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_only_numbers(self):
        password = generate_password(length=100, use_lowercase=False, use_uppercase=False, use_numbers=True, use_symbols=False)
        for char in password:
            self.assertIn(char, string.digits)

    def test_no_character_sets(self):
        with self.assertRaises(ValueError):
            generate_password(use_lowercase=False, use_uppercase=False, use_numbers=False, use_symbols=False)

if __name__ == '__main__':
    unittest.main()
