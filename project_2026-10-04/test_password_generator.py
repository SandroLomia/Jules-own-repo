import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        length = 20
        password = generate_password(length=length)
        self.assertEqual(len(password), length)

    def test_zero_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_negative_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_only_lowercase(self):
        password = generate_password(length=100, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertTrue(all(char in string.ascii_lowercase for char in password))

    def test_no_symbols(self):
        password = generate_password(length=100, use_symbols=False)
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_no_numbers(self):
        password = generate_password(length=100, use_numbers=False)
        self.assertFalse(any(char in string.digits for char in password))

    def test_no_uppercase(self):
        password = generate_password(length=100, use_uppercase=False)
        self.assertFalse(any(char in string.ascii_uppercase for char in password))

    def test_includes_required_characters(self):
        password = generate_password(length=100)
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertTrue(any(char in string.ascii_lowercase for char in password))

    def test_short_length_with_all_requirements(self):
        # Even with length 2, it should just pick a random subset of the required chars
        password = generate_password(length=2)
        self.assertEqual(len(password), 2)

    def test_randomness(self):
        passwords = set()
        for _ in range(100):
            passwords.add(generate_password())
        # The chances of a duplicate 12-char cryptographically secure password in 100 tries is practically zero
        self.assertEqual(len(passwords), 100)

if __name__ == '__main__':
    unittest.main()
