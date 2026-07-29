import unittest
import string
from unittest.mock import patch

from secure_generator import generate_password, generate_token


class TestSecureGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        """Test that generated passwords have the correct length."""
        for length in [4, 8, 16, 32, 64]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)

        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_generate_password_character_sets(self):
        """Test that the generated password contains characters from the requested sets."""
        password = generate_password(length=100)

        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digits = any(c in string.digits for c in password)
        has_symbols = any(c in string.punctuation for c in password)

        self.assertTrue(has_lower)
        self.assertTrue(has_upper)
        self.assertTrue(has_digits)
        self.assertTrue(has_symbols)

    def test_generate_password_no_symbols_no_digits_no_upper(self):
        """Test character set constraints."""
        password = generate_password(
            length=50,
            use_uppercase=False,
            use_numbers=False,
            use_symbols=False
        )
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_generate_token_length(self):
        """Test token generation length logic."""
        # token_urlsafe returns ~1.3 times the bytes length.
        token_16 = generate_token(length=16)
        self.assertGreater(len(token_16), 16)

        token_32 = generate_token(length=32)
        self.assertGreater(len(token_32), len(token_16))

        with self.assertRaises(ValueError):
            generate_token(length=0)

    @patch("secrets.SystemRandom.shuffle")
    def test_cryptographic_shuffle_usage(self, mock_shuffle):
        """Test that secrets.SystemRandom.shuffle is actually called."""
        generate_password(length=16)
        mock_shuffle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
