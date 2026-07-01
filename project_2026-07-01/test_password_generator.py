import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_exclude_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_exclude_lowercase(self):
        password = generate_password(use_lowercase=False)
        self.assertFalse(any(c in string.ascii_lowercase for c in password))

    def test_exclude_numbers(self):
        password = generate_password(use_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_exclude_symbols(self):
        password = generate_password(use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_zero_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_negative_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_types_selected_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_numbers=False, use_symbols=False)

    def test_length_too_short_for_requirements_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=2, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True)

if __name__ == '__main__':
    unittest.main()
