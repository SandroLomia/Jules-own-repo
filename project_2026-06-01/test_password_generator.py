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

    def test_contains_all_character_types_by_default(self):
        # Default includes lower, upper, digit, special. Length 12 is enough.
        password = generate_password(length=12)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)

        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_only_lowercase(self):
        password = generate_password(length=10, use_uppercase=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase_and_digits(self):
        password = generate_password(length=15, use_lowercase=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase or c in string.digits for c in password))

        # Also verify both are present
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        self.assertTrue(has_upper)
        self.assertTrue(has_digit)

    def test_no_character_sets_selected(self):
        with self.assertRaisesRegex(ValueError, "At least one character set must be selected."):
            generate_password(use_lowercase=False, use_uppercase=False, use_digits=False, use_special=False)

    def test_length_too_short_for_requirements(self):
        # 4 required characters, but length requested is 3
        with self.assertRaisesRegex(ValueError, "Password length must be at least"):
            generate_password(length=3)

    def test_zero_or_negative_length(self):
        with self.assertRaisesRegex(ValueError, "Password length must be greater than 0."):
            generate_password(length=0)

        with self.assertRaisesRegex(ValueError, "Password length must be greater than 0."):
            generate_password(length=-5)

if __name__ == "__main__":
    unittest.main()
