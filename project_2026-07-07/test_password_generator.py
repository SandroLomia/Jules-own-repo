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

    def test_character_types(self):
        password = generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True)

        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_exclude_types(self):
        password = generate_password(length=10, include_uppercase=False, include_lowercase=False, include_digits=True, include_special=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_randomness(self):
        password_1 = generate_password()
        password_2 = generate_password()
        self.assertNotEqual(password_1, password_2)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=2, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True)

    def test_no_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(length=10, include_uppercase=False, include_lowercase=False, include_digits=False, include_special=False)

if __name__ == "__main__":
    unittest.main()
