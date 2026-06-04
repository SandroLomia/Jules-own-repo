import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
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

    def test_no_symbols(self):
        password = generate_password(use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_min_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_all_false(self):
        # Even if all are false, it should just fall back to lowercase only or fail depending on logic?
        # Actually in the code, `characters = string.ascii_lowercase` happens first.
        # So setting others to False just uses lowercase.
        password = generate_password(use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

if __name__ == '__main__':
    unittest.main()
