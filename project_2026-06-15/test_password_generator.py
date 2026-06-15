import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 16)

    def test_custom_length(self):
        pwd = generate_password(length=32)
        self.assertEqual(len(pwd), 32)

        pwd = generate_password(length=8)
        self.assertEqual(len(pwd), 8)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_uppercase(self):
        pwd = generate_password(length=100, use_uppercase=False)
        for char in pwd:
            self.assertNotIn(char, string.ascii_uppercase)

    def test_no_digits(self):
        pwd = generate_password(length=100, use_digits=False)
        for char in pwd:
            self.assertNotIn(char, string.digits)

    def test_no_special(self):
        pwd = generate_password(length=100, use_special=False)
        for char in pwd:
            self.assertNotIn(char, string.punctuation)

    def test_only_lowercase(self):
        pwd = generate_password(length=100, use_uppercase=False, use_digits=False, use_special=False)
        for char in pwd:
            self.assertIn(char, string.ascii_lowercase)

if __name__ == "__main__":
    unittest.main()
