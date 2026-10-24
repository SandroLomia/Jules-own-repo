import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_init(self):
        chain = MarkovChain(order=2)
        self.assertEqual(chain.order, 2)
        self.assertEqual(len(chain.model), 0)

    def test_train_basic(self):
        chain = MarkovChain(order=1)
        text = "the quick brown fox"
        chain.train(text)

        expected_model = {
            ("the",): ["quick"],
            ("quick",): ["brown"],
            ("brown",): ["fox"]
        }
        self.assertEqual(dict(chain.model), expected_model)

    def test_train_higher_order(self):
        chain = MarkovChain(order=2)
        text = "the quick brown fox jumps"
        chain.train(text)

        expected_model = {
            ("the", "quick"): ["brown"],
            ("quick", "brown"): ["fox"],
            ("brown", "fox"): ["jumps"]
        }
        self.assertEqual(dict(chain.model), expected_model)

    def test_train_multiple_occurrences(self):
        chain = MarkovChain(order=1)
        text = "a b a c a b"
        chain.train(text)

        expected_model = {
            ("a",): ["b", "c", "b"],
            ("b",): ["a"],
            ("c",): ["a"]
        }
        self.assertEqual(dict(chain.model), expected_model)

    def test_train_short_text(self):
        chain = MarkovChain(order=2)
        chain.train("one")
        self.assertEqual(len(chain.model), 0)

        chain.train("one two")
        self.assertEqual(len(chain.model), 0)

    def test_generate_empty_model(self):
        chain = MarkovChain()
        result = chain.generate()
        self.assertEqual(result, "")

    def test_generate_basic(self):
        chain = MarkovChain(order=1)
        chain.train("a b c d e")

        # It's a straight sequence, so given 'a', it should generate 'a b c d e'
        # up to max_length if it starts there. However, the starting point is random
        # unless seeded. Let's seed it.
        result = chain.generate(max_length=3, seed_state=("b",))
        self.assertEqual(result, "b c d")

    def test_generate_max_length(self):
        chain = MarkovChain(order=1)
        chain.train("a b c d e")

        # Start at 'a'
        result = chain.generate(max_length=10, seed_state=("a",))

        # Since 'e' has no next state, it will stop at 'e'
        self.assertEqual(result, "a b c d e")

    def test_generate_random_start(self):
        chain = MarkovChain(order=1)
        chain.train("x y z")

        # Since it randomly picks a start, and might stop if it hits 'z'
        # we can just test that the output is in the set of valid sequences
        result = chain.generate(max_length=3)
        valid_sequences = ["x y z", "y z", "z"]
        self.assertIn(result, valid_sequences)

    def test_generate_stochastic(self):
        chain = MarkovChain(order=1)
        # 'a' transitions to 'b' or 'c'
        chain.train("a b a c")

        results = set()
        # Run it a few times to ensure we get both branches (probabilistic)
        # Note: Since it's random, there's a tiny chance it always picks the same,
        # but running it 100 times makes it extremely unlikely to fail.
        for _ in range(100):
            res = chain.generate(max_length=2, seed_state=("a",))
            results.add(res)

        self.assertTrue("a b" in results)
        self.assertTrue("a c" in results)

if __name__ == '__main__':
    unittest.main()
