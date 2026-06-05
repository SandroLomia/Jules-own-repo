import unittest
import string
from password_tool import generate_password, check_strength

class TestPasswordTool(unittest.TestCase):

    def test_generate_password_length(self):
        # Test standard lengths
        for length in [4, 8, 16, 32]:
            pwd = generate_password(length)
            self.assertEqual(len(pwd), length)

    def test_generate_password_too_short(self):
        # Test invalid length
        with self.assertRaises(ValueError):
            generate_password(3)

    def test_generate_password_complexity(self):
        # Generate a password and check if it meets the complexity requirements
        pwd = generate_password(16)

        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_lower, "Password lacks lowercase letter")
        self.assertTrue(has_upper, "Password lacks uppercase letter")
        self.assertTrue(has_digit, "Password lacks digit")
        self.assertTrue(has_special, "Password lacks special character")

    def test_check_strength(self):
        # Test 0 or 1 point (short, all lowercase)
        score, desc = check_strength("abc")
        self.assertEqual(score, 0)
        self.assertEqual(desc, "Very Weak")

        # Test 1 point (>= 8 chars, all lowercase)
        score, desc = check_strength("abcdefgh")
        self.assertEqual(score, 1)
        self.assertEqual(desc, "Weak")

        # Test 2 points (>= 8 chars, mixed case)
        score, desc = check_strength("Abcdefgh")
        self.assertEqual(score, 2)
        self.assertEqual(desc, "Fair")

        # Test 3 points (>= 8 chars, mixed case, digit)
        score, desc = check_strength("Abcdefgh1")
        self.assertEqual(score, 3)
        self.assertEqual(desc, "Good")

        # Test 4 points (>= 8 chars, mixed case, digit, special)
        score, desc = check_strength("Abcdefgh1!")
        self.assertEqual(score, 4)
        self.assertEqual(desc, "Strong")

if __name__ == '__main__':
    unittest.main()
