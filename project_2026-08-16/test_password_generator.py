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

    def test_short_length(self):
        password = generate_password(length=2)
        self.assertEqual(len(password), 2)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_upper(self):
        password = generate_password(use_upper=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_no_lower(self):
        password = generate_password(use_lower=False)
        self.assertFalse(any(c in string.ascii_lowercase for c in password))

    def test_no_digits(self):
        password = generate_password(use_digits=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_no_special(self):
        password = generate_password(use_special=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_upper(self):
        password = generate_password(use_lower=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_special=False)

    def test_contains_all_types_by_default(self):
        password = generate_password(length=20)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == "__main__":
    unittest.main()
