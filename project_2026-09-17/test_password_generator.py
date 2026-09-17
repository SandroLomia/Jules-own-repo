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

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_includes_uppercase(self):
        password = generate_password(length=20, include_uppercase=True, include_numbers=False, include_symbols=False)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

    def test_excludes_uppercase(self):
        password = generate_password(length=20, include_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_includes_numbers(self):
        password = generate_password(length=20, include_uppercase=False, include_numbers=True, include_symbols=False)
        self.assertTrue(any(c in string.digits for c in password))

    def test_excludes_numbers(self):
        password = generate_password(length=20, include_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_includes_symbols(self):
        password = generate_password(length=20, include_uppercase=False, include_numbers=False, include_symbols=True)
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_excludes_symbols(self):
        password = generate_password(length=20, include_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(length=20, include_uppercase=False, include_numbers=False, include_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

if __name__ == '__main__':
    unittest.main()
