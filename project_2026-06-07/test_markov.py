import unittest
from markov import MarkovChain

class TestMarkovChain(unittest.TestCase):

    def setUp(self):
        self.mc = MarkovChain(state_size=2)

    def test_add_text(self):
        text = "this is a test this is only a test"
        self.mc.add_text(text)

        # Test model structure
        self.assertIn(("this", "is"), self.mc.model)
        self.assertIn(("is", "a"), self.mc.model)
        self.assertIn(("a", "test"), self.mc.model)

        # Test transition counts
        self.assertEqual(self.mc.model[("this", "is")], ["a", "only"])
        self.assertEqual(self.mc.model[("is", "a")], ["test"])

    def test_generate_text_empty(self):
        # Empty model should generate empty string
        self.assertEqual(self.mc.generate_text(), "")

    def test_generate_text_with_start_state(self):
        text = "this is a test this is only a test"
        self.mc.add_text(text)

        # Ensure it starts with the given state
        generated = self.mc.generate_text(length=4, start_state=("this", "is"))
        self.assertTrue(generated.startswith("this is"))

        words = generated.split()
        self.assertIn(words[2], ["a", "only"])

    def test_generate_text_length(self):
        text = "one two three four five six seven eight nine ten"
        self.mc.add_text(text)

        generated = self.mc.generate_text(length=5)
        self.assertEqual(len(generated.split()), 5)

    def test_generate_text_dead_end(self):
        text = "this is a test"
        self.mc.add_text(text)

        # Generator should stop early if it hits a dead end
        generated = self.mc.generate_text(length=10, start_state=("this", "is"))
        words = generated.split()
        self.assertEqual(len(words), 4)
        self.assertEqual(" ".join(words), "this is a test")

if __name__ == '__main__':
    unittest.main()
