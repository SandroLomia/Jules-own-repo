import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_empty_initialization(self):
        chain = MarkovChain()
        self.assertEqual(chain.order, 1)
        self.assertEqual(chain.state_dict, {})

    def test_invalid_order_initialization(self):
        with self.assertRaises(ValueError):
            MarkovChain(order=0)

    def test_training_transitions(self):
        chain = MarkovChain(order=1)
        # Sequence: "hello" -> "world", "world" -> "hello", "hello" -> "python"
        chain.train("hello world hello python")

        expected_state = {
            ("hello",): ["world", "python"],
            ("world",): ["hello"]
        }
        self.assertEqual(chain.state_dict, expected_state)

    def test_training_higher_order(self):
        chain = MarkovChain(order=2)
        chain.train("the quick brown fox jumps over the quick lazy dog")

        # Checking a specific transition
        self.assertIn("brown", chain.state_dict[("the", "quick")])
        self.assertIn("lazy", chain.state_dict[("the", "quick")])

    def test_generate_empty_state(self):
        chain = MarkovChain()
        self.assertEqual(chain.generate(), "")

    def test_generate_deterministic_sequence(self):
        chain = MarkovChain(order=1)
        chain.train("one two three four")
        # Since each word only has one next word, generation should be deterministic
        # up to the length of the trained sequence, or stop when it reaches "four"

        # Test generation with max_words large enough to hit the end
        generated = chain.generate(max_words=10)

        # Because we start randomly, the sequence could be "one two three four", "two three four", etc.
        # But it should always be a substring of the original text if we just join it
        original_text = "one two three four"
        self.assertIn(generated, original_text)

    def test_generate_length_limit(self):
        chain = MarkovChain(order=1)
        # Infinite loop pattern
        chain.train("loop repeat loop repeat loop repeat")

        generated = chain.generate(max_words=5)
        self.assertEqual(len(generated.split()), 5)

if __name__ == "__main__":
    unittest.main()
