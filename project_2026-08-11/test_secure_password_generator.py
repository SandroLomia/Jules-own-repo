import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_contains_all_character_types(self):
        password = generate_password(length=20)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_exclude_uppercase(self):
        password = generate_password(length=20, include_uppercase=False)
        has_upper = any(c in string.ascii_uppercase for c in password)
        self.assertFalse(has_upper)

    def test_exclude_lowercase(self):
        password = generate_password(length=20, include_lowercase=False)
        has_lower = any(c in string.ascii_lowercase for c in password)
        self.assertFalse(has_lower)

    def test_exclude_digits(self):
        password = generate_password(length=20, include_digits=False)
        has_digit = any(c in string.digits for c in password)
        self.assertFalse(has_digit)

    def test_exclude_special(self):
        password = generate_password(length=20, include_special=False)
        has_special = any(c in string.punctuation for c in password)
        self.assertFalse(has_special)

    def test_min_length_validation(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_no_character_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(include_uppercase=False, include_lowercase=False, include_digits=False, include_special=False)

if __name__ == '__main__':
    unittest.main()
