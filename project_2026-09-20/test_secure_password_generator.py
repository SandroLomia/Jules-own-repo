import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_specific_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

        password_short = generate_password(length=2)
        self.assertEqual(len(password_short), 2)

    def test_omit_numbers(self):
        password = generate_password(length=100, include_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_omit_symbols(self):
        password = generate_password(length=100, include_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

if __name__ == '__main__':
    unittest.main()
