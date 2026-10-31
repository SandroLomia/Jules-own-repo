import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(generate_password(10)), 10)
        self.assertEqual(len(generate_password(1)), 1)
        self.assertEqual(len(generate_password(100)), 100)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0)
        with self.assertRaises(ValueError):
            generate_password(-5)

    def test_all_options_enabled(self):
        pwd = generate_password(20)
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_only_lowercase(self):
        pwd = generate_password(20, use_uppercase=False, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_lowercase_and_uppercase(self):
        pwd = generate_password(20, use_uppercase=True, use_numbers=False, use_symbols=False)
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(all(c in string.ascii_letters for c in pwd))

    def test_lowercase_and_numbers(self):
        pwd = generate_password(20, use_uppercase=False, use_numbers=True, use_symbols=False)
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        valid_chars = string.ascii_lowercase + string.digits
        self.assertTrue(all(c in valid_chars for c in pwd))

    def test_lowercase_and_symbols(self):
        pwd = generate_password(20, use_uppercase=False, use_numbers=False, use_symbols=True)
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))
        valid_chars = string.ascii_lowercase + string.punctuation
        self.assertTrue(all(c in valid_chars for c in pwd))

if __name__ == '__main__':
    unittest.main()
