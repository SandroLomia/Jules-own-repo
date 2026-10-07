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

    def test_includes_uppercase_only(self):
        password = generate_password(use_uppercase=True, use_lowercase=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(char in string.ascii_uppercase for char in password))

    def test_includes_lowercase_only(self):
        password = generate_password(use_uppercase=False, use_lowercase=True, use_digits=False, use_symbols=False)
        self.assertTrue(all(char in string.ascii_lowercase for char in password))

    def test_includes_digits_only(self):
        password = generate_password(use_uppercase=False, use_lowercase=False, use_digits=True, use_symbols=False)
        self.assertTrue(all(char in string.digits for char in password))

    def test_includes_symbols_only(self):
        password = generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=True)
        self.assertTrue(all(char in string.punctuation for char in password))

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=False)

if __name__ == '__main__':
    unittest.main()
