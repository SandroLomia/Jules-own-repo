import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_parameters(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        # Assuming defaults include at least one of each (if length allows)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_specific_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))

    def test_no_numbers(self):
        password = generate_password(use_numbers=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_no_special_chars(self):
        password = generate_password(use_special=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_numbers=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_short_length_guarantees(self):
        # A length of 2 is shorter than the 4 default categories
        password = generate_password(length=2)
        self.assertEqual(len(password), 2)

if __name__ == '__main__':
    unittest.main()
