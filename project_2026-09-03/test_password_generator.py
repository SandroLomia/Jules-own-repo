import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_no_character_sets(self):
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_punctuation=False)

    def test_contains_uppercase(self):
        password = generate_password(use_uppercase=True, use_lowercase=False, use_digits=False, use_punctuation=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_contains_lowercase(self):
        password = generate_password(use_uppercase=False, use_lowercase=True, use_digits=False, use_punctuation=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_contains_digits(self):
        password = generate_password(use_uppercase=False, use_lowercase=False, use_digits=True, use_punctuation=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_contains_punctuation(self):
        password = generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_punctuation=True)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_contains_all_by_default(self):
        password = generate_password()
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == "__main__":
    unittest.main()
