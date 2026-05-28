import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 16)
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        # Note: Since generation is random, it's possible (though highly unlikely)
        # for a 16-char password to not have an upper, digit, or special char.
        # But for basic tests, we just ensure it generates correctly.

    def test_custom_length(self):
        pwd = generate_password(length=32)
        self.assertEqual(len(pwd), 32)

        pwd_short = generate_password(length=1)
        self.assertEqual(len(pwd_short), 1)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_lowercase_only(self):
        pwd = generate_password(length=50, use_uppercase=False, use_digits=False, use_special=False)
        self.assertEqual(len(pwd), 50)
        for char in pwd:
            self.assertTrue(char in string.ascii_lowercase)

    def test_no_special(self):
        pwd = generate_password(length=50, use_special=False)
        for char in pwd:
            self.assertFalse(char in string.punctuation)

    def test_no_digits(self):
        pwd = generate_password(length=50, use_digits=False)
        for char in pwd:
            self.assertFalse(char in string.digits)

    def test_no_upper(self):
        pwd = generate_password(length=50, use_uppercase=False)
        for char in pwd:
            self.assertFalse(char in string.ascii_uppercase)

if __name__ == "__main__":
    unittest.main()
