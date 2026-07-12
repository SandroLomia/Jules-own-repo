import unittest
import string
import math
from secure_password_generator import generate_password, calculate_entropy

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        """Test that the generated password is of the correct length."""
        pw_16 = generate_password(length=16)
        self.assertEqual(len(pw_16), 16)

        pw_32 = generate_password(length=32)
        self.assertEqual(len(pw_32), 32)

        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_generate_password_complexity(self):
        """Test that the generated password obeys the character set constraints."""
        # Test only digits
        pw_digits = generate_password(
            length=20, use_uppercase=False, use_lowercase=False, use_digits=True, use_symbols=False
        )
        for char in pw_digits:
            self.assertIn(char, string.digits)

        # Test only lowercase
        pw_lower = generate_password(
            length=20, use_uppercase=False, use_lowercase=True, use_digits=False, use_symbols=False
        )
        for char in pw_lower:
            self.assertIn(char, string.ascii_lowercase)

        # Test ValueError when no char set is selected
        with self.assertRaises(ValueError):
            generate_password(
                use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=False
            )

    def test_calculate_entropy(self):
        """Test that entropy calculation is correct."""
        # Test with empty password
        self.assertEqual(calculate_entropy(""), 0.0)

        # Test with a password that only has lowercase (pool size 26)
        # We need a password with lowercase chars only, e.g., 'a'
        ent_lower = calculate_entropy("aaaa")
        # pool size for lowercase is 26, length is 4.  E = 4 * log2(26)
        expected_lower = 4 * math.log2(26)
        self.assertAlmostEqual(ent_lower, expected_lower, places=4)

        # Test with mixed password (uppercase + lowercase + digits = 26 + 26 + 10 = 62)
        ent_mixed = calculate_entropy("A1b")
        # pool size 62, length 3
        expected_mixed = 3 * math.log2(62)
        self.assertAlmostEqual(ent_mixed, expected_mixed, places=4)

if __name__ == '__main__':
    unittest.main()
