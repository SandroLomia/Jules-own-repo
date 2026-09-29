import unittest
import string
from password_generator import generate_secure_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_secure_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_secure_password(length=24)
        self.assertEqual(len(password), 24)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_secure_password(length=3)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_secure_password(include_lowercase=False, include_uppercase=False, include_numbers=False, include_symbols=False)

    def test_only_lowercase(self):
        password = generate_secure_password(length=10, include_lowercase=True, include_uppercase=False, include_numbers=False, include_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase(self):
        password = generate_secure_password(length=10, include_lowercase=False, include_uppercase=True, include_numbers=False, include_symbols=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_numbers(self):
        password = generate_secure_password(length=10, include_lowercase=False, include_uppercase=False, include_numbers=True, include_symbols=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_symbols(self):
        password = generate_secure_password(length=10, include_lowercase=False, include_uppercase=False, include_numbers=False, include_symbols=True)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_includes_all_selected_types(self):
        password = generate_secure_password(length=20)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
