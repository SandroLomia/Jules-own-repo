import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = generate_password(length=32)
        self.assertEqual(len(password), 32)

    def test_only_uppercase(self):
        password = generate_password(length=10, use_uppercase=True, use_lowercase=False, use_numbers=False, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_lowercase(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=True, use_numbers=False, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_numbers(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_numbers=True, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_symbols(self):
        password = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_numbers=False, use_symbols=True)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_no_character_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_numbers=False, use_symbols=False)

    def test_length_too_short_for_requirements(self):
        with self.assertRaises(ValueError):
            generate_password(length=3, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True)

if __name__ == '__main__':
    unittest.main()
