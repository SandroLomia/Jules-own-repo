import unittest
import string
from secure_generator import SecureGenerator

class TestSecureGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        """Test that the generated password has the requested length."""
        for length in [1, 8, 16, 32, 100]:
            password = SecureGenerator.generate_password(length=length)
            self.assertEqual(len(password), length)

    def test_generate_password_symbols(self):
        """Test that the generated password respects the use_symbols flag."""
        # Test without symbols
        password_no_symbols = SecureGenerator.generate_password(length=100, use_symbols=False)
        for char in password_no_symbols:
            self.assertNotIn(char, string.punctuation)

        # Test with symbols (statistical chance of not having any in 500 chars is negligible)
        password_with_symbols = SecureGenerator.generate_password(length=500, use_symbols=True)
        has_symbol = any(char in string.punctuation for char in password_with_symbols)
        self.assertTrue(has_symbol, "Password generated with use_symbols=True did not contain any symbols")

    def test_generate_password_invalid_length(self):
        """Test that an invalid length raises a ValueError."""
        with self.assertRaises(ValueError):
            SecureGenerator.generate_password(length=0)
        with self.assertRaises(ValueError):
            SecureGenerator.generate_password(length=-5)

    def test_secure_shuffle_modifies_list(self):
        """Test that secure_shuffle changes the order of a list (mostly) and preserves elements."""
        original_list = list(range(100))
        test_list = original_list.copy()

        shuffled_list = SecureGenerator.secure_shuffle(test_list)

        # Elements should be identical, just reordered
        self.assertCountEqual(original_list, shuffled_list)
        # Order should (almost certainly) be different for a list of 100 items
        self.assertNotEqual(original_list, shuffled_list)
        # Verify it works in-place and returns the same list object
        self.assertIs(test_list, shuffled_list)

    def test_secure_shuffle_invalid_type(self):
        """Test that secure_shuffle raises TypeError for non-list inputs."""
        with self.assertRaises(TypeError):
            SecureGenerator.secure_shuffle("not a list")
        with self.assertRaises(TypeError):
            SecureGenerator.secure_shuffle((1, 2, 3))

if __name__ == '__main__':
    unittest.main()
