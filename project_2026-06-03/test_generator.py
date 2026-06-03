import unittest
import string
from generator import generate_password, generate_passphrase

class TestGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_generate_password_min_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_generate_password_character_sets(self):
        pwd = generate_password(length=50, use_uppercase=True, use_digits=True, use_symbols=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

    def test_generate_password_no_uppercase(self):
        pwd = generate_password(length=50, use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in pwd))

    def test_generate_password_no_digits(self):
        pwd = generate_password(length=50, use_digits=False)
        self.assertFalse(any(c in string.digits for c in pwd))

    def test_generate_password_no_symbols(self):
        pwd = generate_password(length=50, use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_generate_passphrase_word_count(self):
        phrase = generate_passphrase(num_words=6, separator="-")
        words = phrase.split("-")
        self.assertEqual(len(words), 6)

    def test_generate_passphrase_min_words(self):
        with self.assertRaises(ValueError):
            generate_passphrase(num_words=1)

    def test_generate_passphrase_custom_separator(self):
        phrase = generate_passphrase(num_words=4, separator=" ")
        words = phrase.split(" ")
        self.assertEqual(len(words), 4)

if __name__ == "__main__":
    unittest.main()
