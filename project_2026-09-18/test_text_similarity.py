import unittest
from text_similarity import TextSimilarity

class TestTextSimilarity(unittest.TestCase):

    def test_exact_match(self):
        text = "Hello world this is a test"
        similarity = TextSimilarity.compute_cosine_similarity(text, text)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_complete_mismatch(self):
        text1 = "Apples are delicious"
        text2 = "Oranges are terrible"
        # "are" is the only common word
        # text1 tokens: apples:1, are:1, delicious:1 (magnitude sqrt(3))
        # text2 tokens: oranges:1, are:1, terrible:1 (magnitude sqrt(3))
        # dot product = 1
        # similarity = 1 / 3 = 0.3333...
        similarity = TextSimilarity.compute_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.3333333333333333, places=5)

        text3 = "Apples"
        text4 = "Oranges"
        similarity = TextSimilarity.compute_cosine_similarity(text3, text4)
        self.assertAlmostEqual(similarity, 0.0, places=5)

    def test_partial_match(self):
        text1 = "The quick brown fox jumps over the lazy dog"
        text2 = "A fast brown fox jumps over a lazy dog"
        # Partial overlap test
        similarity = TextSimilarity.compute_cosine_similarity(text1, text2)
        self.assertTrue(0.0 < similarity < 1.0)
        self.assertAlmostEqual(similarity, 0.5454545454545454, places=5)

    def test_empty_strings(self):
        # Both empty
        self.assertAlmostEqual(TextSimilarity.compute_cosine_similarity("", ""), 1.0, places=5)
        # One empty
        self.assertAlmostEqual(TextSimilarity.compute_cosine_similarity("Hello", ""), 0.0, places=5)

    def test_case_insensitivity(self):
        text1 = "Hello World"
        text2 = "hello world"
        similarity = TextSimilarity.compute_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_punctuation_handling(self):
        text1 = "Hello, World!"
        text2 = "Hello World"
        similarity = TextSimilarity.compute_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
