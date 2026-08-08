import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)

    def test_no_upper(self):
        password = generate_password(length=50, include_upper=False)
        for char in password:
            self.assertNotIn(char, string.ascii_uppercase)

    def test_no_digits(self):
        password = generate_password(length=50, include_digits=False)
        for char in password:
            self.assertNotIn(char, string.digits)

    def test_no_special(self):
        password = generate_password(length=50, include_special=False)
        for char in password:
            self.assertNotIn(char, string.punctuation)

    def test_all_included_by_default(self):
        password = generate_password(length=50)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digits = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digits)
        self.assertTrue(has_special)

if __name__ == '__main__':
    unittest.main()
