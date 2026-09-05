import unittest
from levenshtein import levenshtein_distance

class TestLevenshteinDistance(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(levenshtein_distance("hello", "hello"), 0)
        self.assertEqual(levenshtein_distance("", ""), 0)

    def test_empty_strings(self):
        self.assertEqual(levenshtein_distance("hello", ""), 5)
        self.assertEqual(levenshtein_distance("", "world"), 5)

    def test_insertions(self):
        self.assertEqual(levenshtein_distance("abc", "abcd"), 1)
        self.assertEqual(levenshtein_distance("bc", "abc"), 1)
        self.assertEqual(levenshtein_distance("ac", "abc"), 1)

    def test_deletions(self):
        self.assertEqual(levenshtein_distance("abcd", "abc"), 1)
        self.assertEqual(levenshtein_distance("abc", "bc"), 1)
        self.assertEqual(levenshtein_distance("abc", "ac"), 1)

    def test_substitutions(self):
        self.assertEqual(levenshtein_distance("abc", "axc"), 1)
        self.assertEqual(levenshtein_distance("abc", "xbc"), 1)
        self.assertEqual(levenshtein_distance("abc", "abx"), 1)

    def test_complex_cases(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance("intention", "execution"), 5)

if __name__ == '__main__':
    unittest.main()
