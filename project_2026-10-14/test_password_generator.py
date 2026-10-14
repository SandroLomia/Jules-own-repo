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

    def test_no_special_chars(self):
        password = generate_password(length=100, use_special=False)
        for char in password:
            self.assertIn(char, string.ascii_letters + string.digits)
            self.assertNotIn(char, string.punctuation)

    def test_with_special_chars_possible(self):
        # Since it's random, a special char isn't strictly guaranteed in a small length.
        # But with length 100, it's highly probable.
        password = generate_password(length=100, use_special=True)
        has_special = any(char in string.punctuation for char in password)
        self.assertTrue(has_special)

if __name__ == '__main__':
    unittest.main()
