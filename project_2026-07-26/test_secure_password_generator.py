import unittest
import string
from secure_password_generator import generate_password, generate_passphrase, DEFAULT_WORDLIST

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        """Test if the generated password has the correct length."""
        for length in [4, 10, 16, 64]:
            with self.subTest(length=length):
                pwd = generate_password(length=length)
                self.assertEqual(len(pwd), length)

    def test_generate_password_character_inclusion(self):
        """Test if all selected character types are present."""
        pwd = generate_password(length=16, uppercase=True, lowercase=True, numbers=True, symbols=True)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_number = any(c in string.digits for c in pwd)
        has_symbol = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_upper, "Missing uppercase character")
        self.assertTrue(has_lower, "Missing lowercase character")
        self.assertTrue(has_number, "Missing number")
        self.assertTrue(has_symbol, "Missing symbol")

    def test_generate_password_exclusion(self):
        """Test if excluded character types are not present."""
        # Only lowercase and numbers
        pwd = generate_password(length=20, uppercase=False, lowercase=True, numbers=True, symbols=False)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_symbol = any(c in string.punctuation for c in pwd)

        self.assertFalse(has_upper, "Contains uppercase character when it shouldn't")
        self.assertFalse(has_symbol, "Contains symbol when it shouldn't")

    def test_generate_password_value_error_no_pools(self):
        """Test if ValueError is raised when no character types are selected."""
        with self.assertRaises(ValueError):
            generate_password(uppercase=False, lowercase=False, numbers=False, symbols=False)

    def test_generate_password_value_error_length_too_short(self):
        """Test if ValueError is raised when length is smaller than required character types."""
        with self.assertRaises(ValueError):
            generate_password(length=3, uppercase=True, lowercase=True, numbers=True, symbols=True)

    def test_generate_passphrase_length(self):
        """Test if the generated passphrase has the correct number of words."""
        for num_words in [1, 4, 8]:
            with self.subTest(num_words=num_words):
                phrase = generate_passphrase(num_words=num_words)
                words = phrase.split("-")
                self.assertEqual(len(words), num_words)

    def test_generate_passphrase_custom_wordlist_and_separator(self):
        """Test passphrase generation with a custom wordlist and separator."""
        custom_wordlist = ["foo", "bar", "baz"]
        phrase = generate_passphrase(num_words=3, wordlist=custom_wordlist, separator="_")
        words = phrase.split("_")

        self.assertEqual(len(words), 3)
        for word in words:
            self.assertIn(word, custom_wordlist)

    def test_generate_passphrase_value_error_num_words(self):
        """Test if ValueError is raised when num_words < 1."""
        with self.assertRaises(ValueError):
            generate_passphrase(num_words=0)

    def test_generate_passphrase_value_error_empty_wordlist(self):
        """Test if ValueError is raised when wordlist is empty."""
        with self.assertRaises(ValueError):
            generate_passphrase(wordlist=[])

if __name__ == "__main__":
    unittest.main()
