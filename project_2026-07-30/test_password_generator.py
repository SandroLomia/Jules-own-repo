import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_only_digits(self):
        password = generate_password(use_upper=False, use_lower=False, use_special=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_uppercase(self):
        password = generate_password(use_lower=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_no_character_sets_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_special=False)

    def test_length_too_short_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=2) # 4 char sets are required by default

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

if __name__ == '__main__':
    unittest.main()
