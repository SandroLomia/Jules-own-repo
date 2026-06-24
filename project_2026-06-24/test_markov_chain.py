import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. "
            "The quick brown fox is very fast. "
            "The lazy dog sleeps all day long."
        )

    def test_initialization(self):
        chain = MarkovChain(n_gram=3)
        self.assertEqual(chain.n_gram, 3)
        self.assertEqual(len(chain.transitions), 0)
        self.assertEqual(len(chain.starts), 0)

    def test_train_short_text(self):
        chain = MarkovChain(n_gram=2)
        chain.train("Short")
        self.assertEqual(len(chain.transitions), 0)
        self.assertEqual(len(chain.starts), 0)

    def test_train_populates_transitions(self):
        chain = MarkovChain(n_gram=2)
        chain.train(self.sample_text)
        self.assertGreater(len(chain.transitions), 0)
        self.assertIn(("The", "quick"), chain.transitions)
        self.assertEqual(chain.transitions[("The", "quick")], ["brown", "brown"])

    def test_train_populates_starts(self):
        chain = MarkovChain(n_gram=2)
        chain.train(self.sample_text)
        self.assertGreater(len(chain.starts), 0)
        self.assertIn(("The", "quick"), chain.starts)

    def test_generate_empty_chain(self):
        chain = MarkovChain(n_gram=2)
        text = chain.generate()
        self.assertEqual(text, "")

    def test_generate_valid_text(self):
        chain = MarkovChain(n_gram=2)
        chain.train(self.sample_text)
        generated_text = chain.generate(max_length=10)
        self.assertTrue(len(generated_text) > 0)
        words = generated_text.split()
        self.assertLessEqual(len(words), 10)

if __name__ == '__main__':
    unittest.main()
