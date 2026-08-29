import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_only_uppercase(self):
        pwd = generate_password(length=10, use_upper=True, use_lower=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))
        self.assertEqual(len(pwd), 10)

    def test_only_lowercase(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=True, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_only_digits(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=False, use_digits=True, use_special=False)
        self.assertTrue(all(c in string.digits for c in pwd))

    def test_no_character_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_special=False)

    def test_length_too_short_for_requirements(self):
        with self.assertRaises(ValueError):
            # Requires 4 chars minimum because 4 types are selected
            generate_password(length=3, use_upper=True, use_lower=True, use_digits=True, use_special=True)

    def test_all_character_types_present(self):
        pwd = generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))

        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        self.assertTrue(any(c in special_chars for c in pwd))

if __name__ == '__main__':
    unittest.main()
