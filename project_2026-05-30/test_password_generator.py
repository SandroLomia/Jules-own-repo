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

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_numbers=False, use_special=False)

    def test_only_lowercase(self):
        password = generate_password(length=50, use_uppercase=False, use_numbers=False, use_special=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_only_uppercase(self):
        password = generate_password(length=50, use_lowercase=False, use_numbers=False, use_special=False)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_only_numbers(self):
        password = generate_password(length=50, use_uppercase=False, use_lowercase=False, use_special=False)
        for char in password:
            self.assertIn(char, string.digits)

    def test_only_special(self):
        password = generate_password(length=50, use_uppercase=False, use_lowercase=False, use_numbers=False)
        for char in password:
            self.assertIn(char, string.punctuation)

if __name__ == '__main__':
    unittest.main()
