import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_includes_all_by_default(self):
        pwd = generate_password(length=100) # Long enough to virtually guarantee all sets if working
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_exclude_uppercase(self):
        pwd = generate_password(length=50, include_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

    def test_exclude_numbers(self):
        pwd = generate_password(length=50, include_numbers=False)
        self.assertFalse(any(c in string.digits for c in pwd))

    def test_exclude_symbols(self):
        pwd = generate_password(length=50, include_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_only_lowercase(self):
        pwd = generate_password(length=50, include_uppercase=False, include_numbers=False, include_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_too_short_for_constraints(self):
        with self.assertRaises(ValueError):
            # Requires at least 4 chars (lower, upper, number, symbol)
            generate_password(length=3)

    def test_randomness(self):
        # Extremely unlikely to generate the exact same 12 char password consecutively
        pwd1 = generate_password()
        pwd2 = generate_password()
        self.assertNotEqual(pwd1, pwd2)

if __name__ == '__main__':
    unittest.main()
