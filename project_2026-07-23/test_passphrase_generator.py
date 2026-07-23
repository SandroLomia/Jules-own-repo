import unittest
from passphrase_generator import SecurePassphraseGenerator

class TestSecurePassphraseGenerator(unittest.TestCase):

    def setUp(self):
        self.custom_words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet"]

    def test_default_word_list(self):
        generator = SecurePassphraseGenerator()
        self.assertEqual(len(generator.word_list), 26)
        self.assertIn("apple", generator.word_list)

    def test_generate_passphrase(self):
        generator = SecurePassphraseGenerator(self.custom_words)

        # Test default length (4) and separator ('-')
        passphrase = generator.generate_passphrase()
        words = passphrase.split('-')
        self.assertEqual(len(words), 4)
        for word in words:
            self.assertIn(word, self.custom_words)

        # Test custom length and separator
        passphrase2 = generator.generate_passphrase(num_words=6, separator='_')
        words2 = passphrase2.split('_')
        self.assertEqual(len(words2), 6)

    def test_generate_unique_passphrase(self):
        generator = SecurePassphraseGenerator(self.custom_words)

        # Generate passphrase with unique words
        passphrase = generator.generate_passphrase(num_words=10, unique=True)
        words = passphrase.split('-')

        self.assertEqual(len(words), 10)
        self.assertEqual(len(set(words)), 10) # All words should be unique

        # Test error when asking for more unique words than available
        with self.assertRaises(ValueError):
            generator.generate_passphrase(num_words=11, unique=True)

    def test_evaluate_entropy(self):
        generator = SecurePassphraseGenerator(self.custom_words) # 10 words pool

        entropy = generator.evaluate_entropy(4)
        # Entropy for 4 words from a pool of 10 is 4 * log2(10)
        # log2(10) is ~3.32, so 4 * ~3.32 is ~13.28
        self.assertGreater(entropy, 13.2)
        self.assertLess(entropy, 13.3)

        # Test zero words
        self.assertEqual(generator.evaluate_entropy(0), 0.0)

if __name__ == '__main__':
    unittest.main()
