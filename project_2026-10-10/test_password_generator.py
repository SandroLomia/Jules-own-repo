import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

        # Verify it has at least one of each required type
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_digits=False, use_special=False)
        self.assertEqual(len(password), 12)

        # Verify only lower case
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

        self.assertFalse(has_upper)
        self.assertTrue(has_lower)
        self.assertFalse(has_digit)
        self.assertFalse(has_special)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=-5)

if __name__ == '__main__':
    unittest.main()
