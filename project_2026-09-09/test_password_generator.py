import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_default_generation(self):
        password = PasswordGenerator.generate_password()
        self.assertEqual(len(password), 12)
        self.assertIsInstance(password, str)

    def test_uppercase_inclusion(self):
        password = PasswordGenerator.generate_password(length=10, use_upper=True, use_lower=False, use_digits=False, use_special=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_digit_inclusion(self):
        password = PasswordGenerator.generate_password(length=8, use_upper=False, use_lower=False, use_digits=True, use_special=False)
        self.assertEqual(len(password), 8)
        self.assertTrue(all(c in string.digits for c in password))

    def test_special_character_inclusion(self):
        password = PasswordGenerator.generate_password(length=15, use_upper=False, use_lower=False, use_digits=False, use_special=True)
        self.assertEqual(len(password), 15)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_password(length=0)

    def test_no_types_selected(self):
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_password(use_upper=False, use_lower=False, use_digits=False, use_special=False)

if __name__ == '__main__':
    unittest.main()
