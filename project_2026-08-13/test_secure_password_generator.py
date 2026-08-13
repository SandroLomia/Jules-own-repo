import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=12)), 12)
        self.assertEqual(len(generate_password(length=64)), 64)

    def test_password_contains_upper(self):
        password = generate_password(length=12, use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_password_contains_lower(self):
        password = generate_password(length=12, use_upper=False, use_lower=True, use_digits=False, use_symbols=False)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_password_contains_digits(self):
        password = generate_password(length=12, use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(all(c in string.digits for c in password))

    def test_password_contains_symbols(self):
        password = generate_password(length=12, use_upper=False, use_lower=False, use_digits=False, use_symbols=True)
        self.assertTrue(any(c in string.punctuation for c in password))
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_password_mixed_requirements(self):
        password = generate_password(length=4, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_password_value_error_if_no_character_set(self):
        with self.assertRaises(ValueError) as context:
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)
        self.assertIn("At least one character type must be selected", str(context.exception))

    def test_password_value_error_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            generate_password(length=0)
        self.assertIn("Password length must be greater than 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            generate_password(length=-5)
        self.assertIn("Password length must be greater than 0", str(context.exception))

    def test_password_value_error_too_short_for_requirements(self):
        with self.assertRaises(ValueError) as context:
            generate_password(length=3, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
        self.assertIn("Password length must be at least", str(context.exception))

if __name__ == '__main__':
    unittest.main()
