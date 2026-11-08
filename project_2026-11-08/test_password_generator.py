import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        for char in password:
            self.assertNotIn(char, string.ascii_uppercase)

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_digits=False, use_special=False)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

if __name__ == '__main__':
    unittest.main()
