import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_password(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_no_numbers(self):
        password = generate_password(use_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_no_special_chars(self):
        password = generate_password(use_special=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_numbers=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

if __name__ == '__main__':
    unittest.main()
