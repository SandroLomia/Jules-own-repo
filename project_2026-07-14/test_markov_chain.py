import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_empty_initialization(self):
        generator = MarkovChain()
        self.assertEqual(generator.transitions, {})
        self.assertEqual(generator.generate_text(), "")

    def test_add_short_text(self):
        generator = MarkovChain(state_size=2)
        generator.add_text("Too short")
        self.assertEqual(generator.transitions, {})

    def test_add_text_transitions(self):
        generator = MarkovChain(state_size=1)
        generator.add_text("A B C A B D")

        expected_transitions = {
            ('A',): ['B', 'B'],
            ('B',): ['C', 'D'],
            ('C',): ['A']
        }
        self.assertEqual(generator.transitions, expected_transitions)

    def test_generate_text_length(self):
        generator = MarkovChain(state_size=1)
        generator.add_text("A B C D E F")

        generated = generator.generate_text(max_words=3)
        words = generated.split()

        self.assertLessEqual(len(words), 3)
        # Should be at least state size
        self.assertGreaterEqual(len(words), 1)

    def test_generate_text_follows_transitions(self):
        generator = MarkovChain(state_size=1)
        # B always follows A
        generator.add_text("A B A B A B")

        generated = generator.generate_text(max_words=4)
        words = generated.split()

        # If 'A' is chosen, the next must be 'B'
        for i in range(len(words) - 1):
            if words[i] == 'A':
                self.assertEqual(words[i+1], 'B')

if __name__ == "__main__":
    unittest.main()
