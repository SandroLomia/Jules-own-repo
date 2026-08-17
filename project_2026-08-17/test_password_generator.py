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

    def test_minimum_length(self):
        password = generate_password(length=4)
        self.assertEqual(len(password), 4)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_contains_required_character_types(self):
        password = generate_password(length=20)

        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_punct = any(c in string.punctuation for c in password)

        self.assertTrue(has_lower, "Password must contain a lowercase letter")
        self.assertTrue(has_upper, "Password must contain an uppercase letter")
        self.assertTrue(has_digit, "Password must contain a digit")
        self.assertTrue(has_punct, "Password must contain a punctuation character")

    def test_randomness(self):
        # Generate 100 passwords and check they are all unique
        passwords = {generate_password() for _ in range(100)}
        self.assertEqual(len(passwords), 100, "Generated passwords should be unique")

if __name__ == '__main__':
    unittest.main()
