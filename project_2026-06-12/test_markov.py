import unittest
from markov import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_train_basic(self):
        mc = MarkovChain(order=1)
        mc.train("a b c")
        self.assertEqual(mc.model[("a",)], ["b"])
        self.assertEqual(mc.model[("b",)], ["c"])

    def test_train_order_2(self):
        mc = MarkovChain(order=2)
        mc.train("a b c d")
        self.assertEqual(mc.model[("a", "b")], ["c"])
        self.assertEqual(mc.model[("b", "c")], ["d"])

    def test_generate_empty_model(self):
        mc = MarkovChain()
        self.assertEqual(mc.generate(), "")

    def test_generate_length(self):
        mc = MarkovChain(order=1)
        mc.train("a b c d e f g")
        generated = mc.generate(length=4, start_state=("a",))
        words = generated.split()
        self.assertLessEqual(len(words), 4)

    def test_generate_follows_chain(self):
        mc = MarkovChain(order=1)
        mc.train("hello world hello world")
        generated = mc.generate(length=4, start_state=("hello",))
        # Depending on random choices, could be hello world hello world
        words = generated.split()
        for i in range(len(words) - 1):
            if words[i] == "hello":
                self.assertEqual(words[i+1], "world")
            elif words[i] == "world":
                self.assertEqual(words[i+1], "hello")

if __name__ == '__main__':
    unittest.main()
