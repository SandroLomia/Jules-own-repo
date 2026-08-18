import unittest
import string
from generator import SecureGenerator

class TestSecureGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SecureGenerator()

    def test_generate_password_length(self):
        """Test if the generated password has the correct length."""
        pwd = self.generator.generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_generate_password_chars(self):
        """Test if the generated password includes required character types."""
        pwd = self.generator.generate_password(length=16)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_digit = any(c in string.digits for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_upper, "Missing uppercase character.")
        self.assertTrue(has_lower, "Missing lowercase character.")
        self.assertTrue(has_digit, "Missing digit.")
        self.assertTrue(has_special, "Missing special character.")

    def test_generate_password_custom_sets(self):
        """Test generating a password with specific character sets disabled."""
        pwd = self.generator.generate_password(
            length=10,
            use_uppercase=False,
            use_special=False
        )
        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)

        self.assertFalse(has_upper, "Included uppercase when it should be disabled.")
        self.assertFalse(has_special, "Included special character when it should be disabled.")

    def test_generate_passphrase_length(self):
        """Test if the generated passphrase has the correct number of words."""
        phrase = self.generator.generate_passphrase(num_words=8)
        words = phrase.split("-")
        self.assertEqual(len(words), 8)

    def test_generate_password_too_short(self):
        """Test if generating a password less than 4 chars raises ValueError."""
        with self.assertRaises(ValueError):
            self.generator.generate_password(length=3)

    def test_generate_passphrase_too_short(self):
         """Test if generating a passphrase less than 3 words raises ValueError."""
         with self.assertRaises(ValueError):
             self.generator.generate_passphrase(num_words=2)

if __name__ == '__main__':
    unittest.main()
