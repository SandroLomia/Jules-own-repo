import unittest
from markov import MarkovChain

class TestMarkovChain(unittest.TestCase):

    def test_train_and_generate(self):
        chain = MarkovChain(order=1)
        text = "this is a simple test case for the markov chain this is another simple test"
        chain.train(text)

        # Test generation with sufficient length
        generated = chain.generate(length=5)
        self.assertTrue(len(generated.split()) <= 5)
        self.assertTrue(len(generated.split()) > 0)

        # Check transitions
        self.assertIn("is", chain.transitions[("this",)])
        self.assertIn("a", chain.transitions[("is",)])
        self.assertIn("another", chain.transitions[("is",)])

    def test_higher_order(self):
        chain = MarkovChain(order=2)
        text = "this is a simple test case for the markov chain this is another simple test"
        chain.train(text)

        self.assertIn("a", chain.transitions[("this", "is")])
        self.assertIn("another", chain.transitions[("this", "is")])

    def test_empty_train(self):
        chain = MarkovChain()
        chain.train("")
        self.assertEqual(chain.generate(), "")

    def test_short_train(self):
        chain = MarkovChain(order=3)
        chain.train("short")
        self.assertEqual(chain.generate(), "")

if __name__ == "__main__":
    unittest.main()
