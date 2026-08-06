import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.mc = MarkovChain()

    def test_train(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.mc.train(text)

        # Test transitions correctly mapped
        self.assertIn("the", self.mc.transitions)
        self.assertIn("quick", self.mc.transitions["the"])
        self.assertIn("lazy", self.mc.transitions["the"])
        self.assertIn("brown", self.mc.transitions["quick"])

        # Test words list contains tokenized words
        self.assertEqual(len(self.mc.words), 9)

    def test_train_with_punctuation(self):
        text = "Hello, world! Hello there."
        self.mc.train(text)

        self.assertIn("hello", self.mc.transitions)
        self.assertIn("world", self.mc.transitions["hello"])
        self.assertIn("there", self.mc.transitions["hello"])

    def test_generate(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.mc.train(text)

        generated = self.mc.generate(max_words=5)
        generated_words = generated.split()

        self.assertTrue(len(generated_words) > 0)
        self.assertTrue(len(generated_words) <= 5)

        # Check that generated words are actually from the text
        for word in generated_words:
            self.assertIn(word, self.mc.words)

    def test_empty_training(self):
        self.mc.train("")
        self.assertEqual(len(self.mc.transitions), 0)

        generated = self.mc.generate(10)
        self.assertEqual(generated, "")

    def test_single_word_training(self):
        self.mc.train("Hello")
        self.assertEqual(len(self.mc.transitions), 0)

        generated = self.mc.generate(10)
        self.assertEqual(generated, "")

if __name__ == '__main__':
    unittest.main()
