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

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

    def test_only_uppercase(self):
        password = generate_password(length=10, use_uppercase=True, use_lowercase=False, use_digits=False, use_special=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_lowercase(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_digits(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_digits=True, use_special=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_special(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=True)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_contains_all_types(self):
        # With default settings, a 16 character password should have at least one of each
        password = generate_password(length=16)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_randomness(self):
        # It is highly unlikely for two generated 16-char passwords to be identical
        password_1 = generate_password()
        password_2 = generate_password()
        self.assertNotEqual(password_1, password_2)

if __name__ == '__main__':
    unittest.main()
