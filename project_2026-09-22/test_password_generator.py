import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=32)
        self.assertEqual(len(password), 32)

        password = generate_password(length=8)
        self.assertEqual(len(password), 8)

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_character_inclusion(self):
        # Test lowercase only
        password = generate_password(length=100, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

        # Test uppercase only
        password = generate_password(length=100, use_lowercase=False, use_uppercase=True, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

        # Test no characters selected
        with self.assertRaises(ValueError):
            generate_password(use_lowercase=False, use_uppercase=False, use_numbers=False, use_symbols=False)

    def test_character_inclusion_with_mocked_always_lowercase(self):
        # We can check if characters correctly appear when enabled.
        # It's hard to test randomness deterministically, but with length 1000, we should see at least one of each.
        password = generate_password(length=1000, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
