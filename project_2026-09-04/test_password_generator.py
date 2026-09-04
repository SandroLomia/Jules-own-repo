import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=32)
        self.assertEqual(len(password), 32)

    def test_only_lowercase(self):
        password = generate_password(length=50, use_upper=False, use_numbers=False, use_symbols=False)
        self.assertEqual(len(password), 50)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase(self):
        password = generate_password(length=50, use_lower=False, use_numbers=False, use_symbols=False)
        self.assertEqual(len(password), 50)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_numbers(self):
        password = generate_password(length=50, use_upper=False, use_lower=False, use_symbols=False)
        self.assertEqual(len(password), 50)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_symbols(self):
        password = generate_password(length=50, use_upper=False, use_lower=False, use_numbers=False)
        self.assertEqual(len(password), 50)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_no_character_type_selected(self):
        with self.assertRaises(ValueError) as context:
            generate_password(use_upper=False, use_lower=False, use_numbers=False, use_symbols=False)
        self.assertEqual(str(context.exception), "At least one character type must be selected.")

    def test_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            generate_password(length=0)
        self.assertEqual(str(context.exception), "Password length must be greater than 0.")

        with self.assertRaises(ValueError):
            generate_password(length=-5)

if __name__ == '__main__':
    unittest.main()
