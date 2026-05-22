import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_initialization(self):
        mc = MarkovChain(order=2)
        self.assertEqual(mc.order, 2)
        self.assertEqual(len(mc.chain), 0)

        with self.assertRaises(ValueError):
            MarkovChain(order=0)

    def test_train(self):
        mc = MarkovChain(order=1)
        text = "hello world hello python"
        mc.train(text)

        self.assertEqual(mc.starts, [("hello",)])
        self.assertEqual(mc.chain[("hello",)], ["world", "python"])
        self.assertEqual(mc.chain[("world",)], ["hello"])

    def test_train_order_2(self):
        mc = MarkovChain(order=2)
        text = "I love python because python is great"
        mc.train(text)

        self.assertEqual(mc.starts, [("I", "love")])
        self.assertEqual(mc.chain[("I", "love")], ["python"])
        self.assertEqual(mc.chain[("love", "python")], ["because"])

    def test_generate_empty(self):
        mc = MarkovChain(order=2)
        self.assertEqual(mc.generate(), "")

    def test_generate_deterministic(self):
        # A chain with only one possible path
        mc = MarkovChain(order=1)
        text = "a b c d e f"
        mc.train(text)

        # It should generate "a b c d e f" exactly, given the order
        # Assuming it starts with "a"
        result = mc.generate(max_words=6, start_state=("a",))
        self.assertEqual(result, "a b c d e f")

    def test_generate_max_words(self):
        mc = MarkovChain(order=1)
        text = "loop back loop back loop back"
        mc.train(text)

        # Start state "loop" will yield "back", "back" will yield "loop"
        result = mc.generate(max_words=4, start_state=("loop",))
        self.assertEqual(len(result.split()), 4)

if __name__ == "__main__":
    unittest.main()
