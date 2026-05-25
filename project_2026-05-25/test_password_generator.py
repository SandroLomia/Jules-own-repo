import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
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
        password = generate_password(length=10, use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_no_numbers(self):
        password = generate_password(length=10, use_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_no_symbols(self):
        password = generate_password(length=10, use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(length=10, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_insufficient_length_for_constraints(self):
        # We need at least 4 chars for lower, upper, number, symbol
        with self.assertRaises(ValueError):
            generate_password(length=3, use_uppercase=True, use_numbers=True, use_symbols=True)

if __name__ == '__main__':
    unittest.main()
