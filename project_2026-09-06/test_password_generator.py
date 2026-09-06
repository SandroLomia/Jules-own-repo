import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_password_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_password_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_minimum_password_length_exception(self):
        with self.assertRaises(ValueError):
            generate_password(length=7)

    def test_includes_uppercase(self):
        password = generate_password(length=100, include_uppercase=True, include_numbers=False, include_symbols=False)
        has_uppercase = any(char in string.ascii_uppercase for char in password)
        self.assertTrue(has_uppercase, "Password should contain uppercase letters")

    def test_includes_numbers(self):
        password = generate_password(length=100, include_uppercase=False, include_numbers=True, include_symbols=False)
        has_numbers = any(char in string.digits for char in password)
        self.assertTrue(has_numbers, "Password should contain numbers")

    def test_includes_symbols(self):
        password = generate_password(length=100, include_uppercase=False, include_numbers=False, include_symbols=True)
        has_symbols = any(char in string.punctuation for char in password)
        self.assertTrue(has_symbols, "Password should contain symbols")

    def test_all_character_types(self):
        password = generate_password(length=100, include_uppercase=True, include_numbers=True, include_symbols=True)
        has_lowercase = any(char in string.ascii_lowercase for char in password)
        has_uppercase = any(char in string.ascii_uppercase for char in password)
        has_numbers = any(char in string.digits for char in password)
        has_symbols = any(char in string.punctuation for char in password)

        self.assertTrue(has_lowercase)
        self.assertTrue(has_uppercase)
        self.assertTrue(has_numbers)
        self.assertTrue(has_symbols)

if __name__ == '__main__':
    unittest.main()
