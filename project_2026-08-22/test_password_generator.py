import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_length(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_password(-5)

    def test_only_uppercase(self):
        password = generate_password(20, use_lower=False, use_numbers=False, use_specials=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_lowercase(self):
        password = generate_password(20, use_upper=False, use_numbers=False, use_specials=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_numbers(self):
        password = generate_password(20, use_upper=False, use_lower=False, use_specials=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_specials(self):
        password = generate_password(20, use_upper=False, use_lower=False, use_numbers=False)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_no_character_sets_enabled(self):
        with self.assertRaises(ValueError):
            generate_password(12, use_upper=False, use_lower=False, use_numbers=False, use_specials=False)

if __name__ == '__main__':
    unittest.main()
