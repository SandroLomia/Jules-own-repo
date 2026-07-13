import unittest
import string
from secure_pass_gen import PasswordGenerator

class TestSecurePassGen(unittest.TestCase):
    def test_generate_password_length(self):
        # Test default length
        pwd = PasswordGenerator.generate_password()
        self.assertEqual(len(pwd), 16)

        # Test custom length
        pwd2 = PasswordGenerator.generate_password(length=24)
        self.assertEqual(len(pwd2), 24)

    def test_generate_password_character_sets(self):
        # Test only lowercase
        pwd = PasswordGenerator.generate_password(length=10, use_upper=False, use_lower=True, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

        # Test only uppercase
        pwd2 = PasswordGenerator.generate_password(length=10, use_upper=True, use_lower=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd2))

        # Test only digits
        pwd3 = PasswordGenerator.generate_password(length=10, use_upper=False, use_lower=False, use_digits=True, use_special=False)
        self.assertTrue(all(c in string.digits for c in pwd3))

    def test_generate_password_edge_cases(self):
        # Test invalid length
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_password(length=0)

        # Test no char sets selected
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_password(use_upper=False, use_lower=False, use_digits=False, use_special=False)

        # Test length too short for all required types
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_password(length=3, use_upper=True, use_lower=True, use_digits=True, use_special=True)

    def test_generate_passphrase_word_count(self):
        wordlist = ["apple", "banana", "cherry", "date", "elderberry"]

        # Test word count and default separator
        passphrase = PasswordGenerator.generate_passphrase(num_words=3, wordlist=wordlist)
        words = passphrase.split("-")
        self.assertEqual(len(words), 3)
        self.assertTrue(all(word in wordlist for word in words))

        # Test custom separator
        passphrase2 = PasswordGenerator.generate_passphrase(num_words=4, wordlist=wordlist, separator="_")
        words2 = passphrase2.split("_")
        self.assertEqual(len(words2), 4)

    def test_generate_passphrase_edge_cases(self):
        wordlist = ["apple", "banana"]

        # Test invalid word count
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_passphrase(num_words=0, wordlist=wordlist)

        # Test empty wordlist
        with self.assertRaises(ValueError):
            PasswordGenerator.generate_passphrase(num_words=3, wordlist=[])

if __name__ == "__main__":
    unittest.main()
