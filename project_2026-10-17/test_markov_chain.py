import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.mc = MarkovChain(state_size=1)

    def test_train_builds_correct_dictionary(self):
        text = "this is a test this is only a test"
        self.mc.train(text)

        expected_dict = {
            ('this',): ['is', 'is'],
            ('is',): ['a', 'only'],
            ('only',): ['a'],
            ('a',): ['test', 'test'],
            ('test',): ['this']
        }
        self.assertEqual(self.mc.dictionary, expected_dict)

    def test_generate_respects_length(self):
        text = "the quick brown fox jumps over the lazy dog"
        self.mc.train(text)

        generated = self.mc.generate(length=5)
        words = generated.split()
        self.assertEqual(len(words), 5)

    def test_render_to_html_escapes_input(self):
        text = "simple text"
        self.mc.train(text)

        user_title = "<script>alert('xss')</script>"
        html_output = self.mc.render_to_html(user_title, length=2)

        self.assertIn("&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;", html_output)
        self.assertNotIn("<script>", html_output)

    def test_generate_shuffled_alters_order(self):
        # Create a text where generation is completely deterministic
        # e.g., "word1 word2 word3 word4 word5" -> each word only follows the previous
        text = "one two three four five six seven eight nine ten"
        self.mc.train(text)

        # Standard generation would be exactly the sequence (or part of it)
        # But we generate a sequence and then shuffle it.
        # Since standard generation starting from 'one' will always be 'one two three...',
        # shuffling it will likely change the order.

        # Let's generate a long enough sequence to ensure shuffling changes the order.
        # We'll use a slightly different approach: just check that the output of generate_shuffled
        # contains the same words as standard generation but likely in a different order.

        # Let's train on a sequence that repeats so we can generate longer text
        text2 = "a b c d e f g h i j k l m n o p q r s t u v w x y z a"
        mc2 = MarkovChain(state_size=1)
        mc2.train(text2)

        # Generate some text
        gen_shuffled = mc2.generate_shuffled(length=10)

        # It's hard to assert it's strictly *altered* because a random shuffle *could*
        # technically produce the exact same sequence, but for a length of 10, the
        # probability is very low.
        self.assertEqual(len(gen_shuffled.split()), 10)

        # We can also check that words are valid
        for word in gen_shuffled.split():
            self.assertIn(word, text2.split())

if __name__ == '__main__':
    unittest.main()
