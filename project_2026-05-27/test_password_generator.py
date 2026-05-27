import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_minimum_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_includes_uppercase(self):
        password = generate_password(length=20, include_uppercase=True)
        has_upper = any(c in string.ascii_uppercase for c in password)
        self.assertTrue(has_upper)

    def test_includes_digits(self):
        password = generate_password(length=20, include_digits=True)
        has_digit = any(c in string.digits for c in password)
        self.assertTrue(has_digit)

    def test_includes_special(self):
        password = generate_password(length=20, include_special=True)
        has_special = any(c in string.punctuation for c in password)
        self.assertTrue(has_special)

    def test_no_uppercase(self):
        password = generate_password(length=20, include_uppercase=False)
        has_upper = any(c in string.ascii_uppercase for c in password)
        self.assertFalse(has_upper)

    def test_no_digits(self):
        password = generate_password(length=20, include_digits=False)
        has_digit = any(c in string.digits for c in password)
        self.assertFalse(has_digit)

    def test_no_special(self):
        password = generate_password(length=20, include_special=False)
        has_special = any(c in string.punctuation for c in password)
        self.assertFalse(has_special)

if __name__ == "__main__":
    unittest.main()
