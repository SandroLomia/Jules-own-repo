import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_length(self):
        password = self.generator.generate_password(length=15)
        self.assertEqual(len(password), 15)

    def test_upper(self):
        password = self.generator.generate_password(length=10, use_upper=True, use_numbers=False, use_symbols=False)
        has_upper = any(c.isupper() for c in password)
        self.assertTrue(has_upper)

        # Test without uppercase
        password_no_upper = self.generator.generate_password(length=10, use_upper=False, use_numbers=False, use_symbols=False)
        has_upper = any(c.isupper() for c in password_no_upper)
        self.assertFalse(has_upper)

    def test_numbers(self):
        password = self.generator.generate_password(length=10, use_upper=False, use_numbers=True, use_symbols=False)
        has_number = any(c.isdigit() for c in password)
        self.assertTrue(has_number)

        # Test without numbers
        password_no_number = self.generator.generate_password(length=10, use_upper=False, use_numbers=False, use_symbols=False)
        has_number = any(c.isdigit() for c in password_no_number)
        self.assertFalse(has_number)

    def test_symbols(self):
        symbols = "!@#$%^&*()_+~`|}{[]:;?><,./-="
        password = self.generator.generate_password(length=10, use_upper=False, use_numbers=False, use_symbols=True)
        has_symbol = any(c in symbols for c in password)
        self.assertTrue(has_symbol)

        # Test without symbols
        password_no_symbol = self.generator.generate_password(length=10, use_upper=False, use_numbers=False, use_symbols=False)
        has_symbol = any(c in symbols for c in password_no_symbol)
        self.assertFalse(has_symbol)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(length=2, use_upper=True, use_numbers=True, use_symbols=True)

if __name__ == '__main__':
    unittest.main()
