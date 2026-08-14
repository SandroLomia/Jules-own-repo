import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_numbers=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_no_numbers(self):
        password = generate_password(use_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_no_special(self):
        password = generate_password(use_special=False)
        self.assertFalse(any(c in string.punctuation for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))

    def test_short_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=2, use_uppercase=True, use_numbers=True, use_special=True)

    def test_zero_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

if __name__ == '__main__':
    unittest.main()
