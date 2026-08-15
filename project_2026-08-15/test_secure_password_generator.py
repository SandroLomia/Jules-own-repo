import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        # Test default length
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

        # Test custom length
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

        # Test very short length
        pwd = generate_password(length=1)
        self.assertEqual(len(pwd), 1)

    def test_generate_password_uppercase(self):
        # Ensure uppercase is included when use_uppercase=True
        pwd = generate_password(length=20, use_uppercase=True, use_numbers=False, use_symbols=False)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))

        # Ensure uppercase is excluded when use_uppercase=False
        pwd = generate_password(length=20, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in pwd))

    def test_generate_password_numbers(self):
        # Ensure digits are included when use_numbers=True
        pwd = generate_password(length=20, use_uppercase=False, use_numbers=True, use_symbols=False)
        self.assertTrue(any(c in string.digits for c in pwd))

        # Ensure digits are excluded when use_numbers=False
        pwd = generate_password(length=20, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertFalse(any(c in string.digits for c in pwd))

    def test_generate_password_symbols(self):
        # Ensure symbols are included when use_symbols=True
        pwd = generate_password(length=20, use_uppercase=False, use_numbers=False, use_symbols=True)
        self.assertTrue(any(c in string.punctuation for c in pwd))

        # Ensure symbols are excluded when use_symbols=False
        pwd = generate_password(length=20, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

if __name__ == '__main__':
    unittest.main()
