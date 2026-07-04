import unittest
import string
from password_generator import generate_password, calculate_entropy

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=32)), 32)

        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_generate_password_character_sets(self):
        password = generate_password(length=16, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)

        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)

    def test_generate_password_exclude_sets(self):
        password = generate_password(length=16, include_uppercase=False, include_lowercase=True, include_digits=False, include_symbols=False)

        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        self.assertFalse(has_upper)
        self.assertTrue(has_lower)
        self.assertFalse(has_digit)
        self.assertFalse(has_symbol)

    def test_calculate_entropy(self):
        # A password with only lowercase letters (pool size 26)
        pw1 = "abcdefg"
        self.assertAlmostEqual(calculate_entropy(pw1), 7 * 4.700439718141092, places=5)

        # A password with lowercase and digits (pool size 36)
        pw2 = "abc123"
        self.assertAlmostEqual(calculate_entropy(pw2), 6 * 5.169925001442312, places=5)

        # Empty password
        self.assertEqual(calculate_entropy(""), 0.0)

if __name__ == '__main__':
    unittest.main()
