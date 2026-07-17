import unittest
import string
from secure_password_generator import generate_password, shuffle_string

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        for length in [10, 20, 50, 100]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)

    def test_password_character_sets_all_included(self):
        password = generate_password(length=100, use_uppercase=True, use_numbers=True, use_special=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))

    def test_password_character_sets_excluded(self):
        password = generate_password(length=100, use_uppercase=False, use_numbers=False, use_special=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))
        self.assertFalse(any(c in string.digits for c in password))
        self.assertFalse(any(c in string.punctuation for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))

    def test_shuffle_string(self):
        original = "abcdefghijklmnopqrstuvwxyz1234567890"
        shuffled = shuffle_string(original)

        self.assertEqual(len(original), len(shuffled))
        self.assertNotEqual(original, shuffled)

        self.assertEqual(sorted(original), sorted(shuffled))

    def test_value_error_on_short_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=2, use_uppercase=True, use_numbers=True, use_special=True)

if __name__ == "__main__":
    unittest.main()
