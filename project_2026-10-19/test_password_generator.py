import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        for length in [5, 10, 20]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)

    def test_symbols(self):
        password = generate_password(length=20, use_symbols=True, use_numbers=False, use_uppercase=False)
        has_symbol = any(char in string.punctuation for char in password)
        self.assertTrue(has_symbol, f"Password '{password}' does not contain symbols")

        password_no_symbols = generate_password(length=20, use_symbols=False, use_numbers=True, use_uppercase=True)
        has_symbol_no = any(char in string.punctuation for char in password_no_symbols)
        self.assertFalse(has_symbol_no, f"Password '{password_no_symbols}' should not contain symbols")

    def test_numbers(self):
        password = generate_password(length=20, use_symbols=False, use_numbers=True, use_uppercase=False)
        has_number = any(char in string.digits for char in password)
        self.assertTrue(has_number, f"Password '{password}' does not contain numbers")

        password_no_numbers = generate_password(length=20, use_symbols=True, use_numbers=False, use_uppercase=True)
        has_number_no = any(char in string.digits for char in password_no_numbers)
        self.assertFalse(has_number_no, f"Password '{password_no_numbers}' should not contain numbers")

    def test_uppercase(self):
        password = generate_password(length=20, use_symbols=False, use_numbers=False, use_uppercase=True)
        has_uppercase = any(char in string.ascii_uppercase for char in password)
        self.assertTrue(has_uppercase, f"Password '{password}' does not contain uppercase characters")

        password_no_uppercase = generate_password(length=20, use_symbols=True, use_numbers=True, use_uppercase=False)
        has_uppercase_no = any(char in string.ascii_uppercase for char in password_no_uppercase)
        self.assertFalse(has_uppercase_no, f"Password '{password_no_uppercase}' should not contain uppercase characters")

if __name__ == '__main__':
    unittest.main()
