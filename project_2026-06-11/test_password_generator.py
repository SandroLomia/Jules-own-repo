import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 16)

    def test_custom_length(self):
        pwd = generate_password(length=25)
        self.assertEqual(len(pwd), 25)

    def test_minimum_length_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_contains_uppercase(self):
        pwd = generate_password(use_uppercase=True)
        has_upper = any(c in string.ascii_uppercase for c in pwd)
        self.assertTrue(has_upper)

    def test_no_uppercase(self):
        pwd = generate_password(use_uppercase=False)
        has_upper = any(c in string.ascii_uppercase for c in pwd)
        self.assertFalse(has_upper)

    def test_contains_digits(self):
        pwd = generate_password(use_digits=True)
        has_digit = any(c in string.digits for c in pwd)
        self.assertTrue(has_digit)

    def test_no_digits(self):
        pwd = generate_password(use_digits=False)
        has_digit = any(c in string.digits for c in pwd)
        self.assertFalse(has_digit)

    def test_contains_special(self):
        pwd = generate_password(use_special=True)
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        has_special = any(c in special_chars for c in pwd)
        self.assertTrue(has_special)

    def test_no_special(self):
        pwd = generate_password(use_special=False)
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        has_special = any(c in special_chars for c in pwd)
        self.assertFalse(has_special)

    def test_randomness(self):
        # A simple check to see that two consecutively generated passwords are not the same
        pwd1 = generate_password()
        pwd2 = generate_password()
        self.assertNotEqual(pwd1, pwd2)

if __name__ == '__main__':
    unittest.main()
