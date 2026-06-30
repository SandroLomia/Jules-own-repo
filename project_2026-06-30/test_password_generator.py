import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_only_uppercase(self):
        pwd = generate_password(length=10, use_uppercase=True, use_lowercase=False, use_numbers=False, use_special=False)
        self.assertEqual(len(pwd), 10)
        for char in pwd:
            self.assertIn(char, string.ascii_uppercase)

    def test_only_lowercase(self):
        pwd = generate_password(length=10, use_uppercase=False, use_lowercase=True, use_numbers=False, use_special=False)
        self.assertEqual(len(pwd), 10)
        for char in pwd:
            self.assertIn(char, string.ascii_lowercase)

    def test_only_numbers(self):
        pwd = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_numbers=True, use_special=False)
        self.assertEqual(len(pwd), 10)
        for char in pwd:
            self.assertIn(char, string.digits)

    def test_only_special(self):
        pwd = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_numbers=False, use_special=True)
        self.assertEqual(len(pwd), 10)
        for char in pwd:
            self.assertIn(char, string.punctuation)

    def test_no_character_sets(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_numbers=False, use_special=False)

    def test_length_too_short(self):
        with self.assertRaises(ValueError):
            # Requiring 4 character sets means min length is 4
            generate_password(length=3)

    def test_length_zero(self):
        with self.assertRaises(ValueError):
            generate_password(length=0, use_uppercase=False, use_lowercase=False, use_numbers=True, use_special=False)

if __name__ == '__main__':
    unittest.main()
