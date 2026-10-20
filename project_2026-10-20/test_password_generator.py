import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        # By default length is 12, uses upper, digits, symbols, and lower
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

        # Verify it contains at least one of each required type
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_digit = any(c in string.digits for c in pwd)
        has_symbol = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_only_lowercase(self):
        pwd = generate_password(length=8, use_uppercase=False, use_digits=False, use_symbols=False)
        self.assertEqual(len(pwd), 8)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_no_symbols(self):
        pwd = generate_password(length=10, use_symbols=False)
        self.assertEqual(len(pwd), 10)
        has_symbol = any(c in string.punctuation for c in pwd)
        self.assertFalse(has_symbol)

        # Should still have lower, upper, digit
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_digit = any(c in string.digits for c in pwd)

        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digit)

    def test_minimum_length_validation(self):
        # 4 types requested by default, length 3 should fail
        with self.assertRaises(ValueError) as context:
            generate_password(length=3)
        self.assertIn("Password length must be at least 4", str(context.exception))

        # 1 type requested, length 0 should fail
        with self.assertRaises(ValueError) as context:
            generate_password(length=0, use_uppercase=False, use_digits=False, use_symbols=False)
        self.assertIn("Password length must be at least 1", str(context.exception))

    def test_randomness(self):
        # Generate two passwords, they should virtually never be the same
        pwd1 = generate_password()
        pwd2 = generate_password()
        self.assertNotEqual(pwd1, pwd2)

if __name__ == '__main__':
    unittest.main()
