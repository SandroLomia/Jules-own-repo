import unittest
import string
from generator import generate_password, generate_passphrase, WORD_LIST

class TestGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=24)), 24)

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_generate_password_no_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

    def test_generate_password_character_types(self):
        pwd_upper = generate_password(length=50, use_lower=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd_upper))

        pwd_lower = generate_password(length=50, use_upper=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd_lower))

        pwd_digits = generate_password(length=50, use_upper=False, use_lower=False, use_symbols=False)
        self.assertTrue(all(c in string.digits for c in pwd_digits))

        pwd_symbols = generate_password(length=50, use_upper=False, use_lower=False, use_digits=False)
        self.assertTrue(all(c in string.punctuation for c in pwd_symbols))

    def test_generate_passphrase_word_count(self):
        phrase = generate_passphrase(num_words=4, separator='-')
        words = phrase.split('-')
        self.assertEqual(len(words), 4)

        phrase2 = generate_passphrase(num_words=8, separator='_')
        words2 = phrase2.split('_')
        self.assertEqual(len(words2), 8)

    def test_generate_passphrase_words_in_list(self):
        phrase = generate_passphrase(num_words=10, separator=' ')
        words = phrase.split(' ')
        for word in words:
            self.assertIn(word, WORD_LIST)

    def test_generate_passphrase_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_passphrase(num_words=0)
        with self.assertRaises(ValueError):
            generate_passphrase(num_words=-1)

if __name__ == '__main__':
    unittest.main()
