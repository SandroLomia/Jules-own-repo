import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.mc = MarkovChain(n_gram=2)
        self.sample_text = "this is a test this is only a test of the markov chain generator"

    def test_initialization(self):
        """Test default and custom initialization."""
        self.assertEqual(self.mc.n_gram, 2)
        self.assertEqual(len(self.mc.state_dict), 0)

        mc3 = MarkovChain(n_gram=3)
        self.assertEqual(mc3.n_gram, 3)

    def test_build_model(self):
        """Test that build_model populates the state dictionary correctly."""
        self.mc.build_model(self.sample_text)

        # Check specific transitions
        self.assertIn(('this', 'is'), self.mc.state_dict)
        self.assertEqual(self.mc.state_dict[('this', 'is')], ['a', 'only'])

        self.assertIn(('is', 'a'), self.mc.state_dict)
        self.assertEqual(self.mc.state_dict[('is', 'a')], ['test'])

    def test_build_model_empty_text(self):
        """Test build_model with empty text."""
        self.mc.build_model("")
        self.assertEqual(len(self.mc.state_dict), 0)

    def test_build_model_short_text(self):
        """Test build_model with text shorter than n_gram."""
        self.mc.build_model("short")
        self.assertEqual(len(self.mc.state_dict), 0)

    def test_generate_text_length(self):
        """Test that generated text length is correct."""
        self.mc.build_model(self.sample_text)
        generated = self.mc.generate_text(length=6)

        # Depending on dead ends, it might be shorter, but not longer.
        # Since our corpus doesn't loop infinitely, it could stop early.
        words = generated.split()
        self.assertLessEqual(len(words), 6)
        self.assertGreaterEqual(len(words), 2)  # At least n_gram

    def test_generate_text_empty_model(self):
        """Test generate_text when model is empty."""
        generated = self.mc.generate_text()
        self.assertEqual(generated, "")

if __name__ == '__main__':
    unittest.main()
