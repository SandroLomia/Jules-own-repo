import unittest
from unittest.mock import patch
from password_generator import generate_passphrase

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.wordlist = ["apple", "banana", "cherry", "date", "elderberry"]

    def test_default_generation(self):
        passphrase = generate_passphrase(self.wordlist)
        words = passphrase.split("-")
        self.assertEqual(len(words), 4)
        for word in words:
            self.assertIn(word, self.wordlist)

    def test_custom_num_words(self):
        passphrase = generate_passphrase(self.wordlist, num_words=2)
        words = passphrase.split("-")
        self.assertEqual(len(words), 2)

    def test_custom_separator(self):
        passphrase = generate_passphrase(self.wordlist, separator="_")
        words = passphrase.split("_")
        self.assertEqual(len(words), 4)
        self.assertNotIn("-", passphrase)

    def test_empty_wordlist(self):
        with self.assertRaises(ValueError):
            generate_passphrase([])

    def test_invalid_num_words(self):
        with self.assertRaises(ValueError):
            generate_passphrase(self.wordlist, num_words=0)
        with self.assertRaises(ValueError):
            generate_passphrase(self.wordlist, num_words=-1)

    @patch("secrets.choice")
    def test_secrets_choice_usage(self, mock_choice):
        mock_choice.side_effect = ["apple", "cherry", "banana", "date"]
        passphrase = generate_passphrase(self.wordlist, num_words=4)
        self.assertEqual(passphrase, "apple-cherry-banana-date")
        self.assertEqual(mock_choice.call_count, 4)

if __name__ == "__main__":
    unittest.main()
