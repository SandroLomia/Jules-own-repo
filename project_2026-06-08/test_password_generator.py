import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)

    def test_minimum_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=7)

    def test_no_special_chars(self):
        password = generate_password(length=100, use_special=False)
        for char in password:
            self.assertNotIn(char, string.punctuation)

    def test_no_numbers(self):
        password = generate_password(length=100, use_numbers=False)
        for char in password:
            self.assertNotIn(char, string.digits)

    def test_no_uppercase(self):
        password = generate_password(length=100, use_uppercase=False)
        for char in password:
            self.assertNotIn(char, string.ascii_uppercase)

    def test_only_lowercase(self):
        password = generate_password(length=100, use_uppercase=False, use_numbers=False, use_special=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

if __name__ == "__main__":
    unittest.main()
