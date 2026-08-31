import unittest
from levenshtein import calculate_levenshtein_distance

class TestLevenshteinDistance(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(calculate_levenshtein_distance("hello", "hello"), 0)
        self.assertEqual(calculate_levenshtein_distance("", ""), 0)

    def test_empty_string(self):
        self.assertEqual(calculate_levenshtein_distance("hello", ""), 5)
        self.assertEqual(calculate_levenshtein_distance("", "world"), 5)

    def test_basic_distance(self):
        # Substitution
        self.assertEqual(calculate_levenshtein_distance("kitten", "sitten"), 1)
        # Substitution and insertion
        self.assertEqual(calculate_levenshtein_distance("sitten", "sittin"), 1)
        # Substitution, insertion, and insertion
        self.assertEqual(calculate_levenshtein_distance("kitten", "sitting"), 3)

    def test_case_sensitivity(self):
        self.assertEqual(calculate_levenshtein_distance("Hello", "hello"), 1)

    def test_completely_different(self):
        self.assertEqual(calculate_levenshtein_distance("abc", "def"), 3)
        self.assertEqual(calculate_levenshtein_distance("123", "456"), 3)

if __name__ == "__main__":
    unittest.main()
