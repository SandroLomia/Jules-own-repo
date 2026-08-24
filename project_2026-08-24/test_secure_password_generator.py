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

    def test_uppercase_inclusion(self):
        password = generate_password(length=10, use_uppercase=True, use_lowercase=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_lowercase_inclusion(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_digits_inclusion(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_digits=True, use_special=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_special_chars_inclusion(self):
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=True)
        self.assertTrue(all(c in special_chars for c in password))

    def test_all_character_types(self):
        password = generate_password(length=20)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

    def test_length_too_short_for_types(self):
        with self.assertRaises(ValueError):
            # Attempt to generate a 2 character password but request 4 types
            generate_password(length=2)

if __name__ == '__main__':
    unittest.main()
