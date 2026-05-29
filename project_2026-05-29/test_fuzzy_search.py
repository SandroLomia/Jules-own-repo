import unittest
from fuzzy_search import levenshtein_distance, fuzzy_search

class TestFuzzySearch(unittest.TestCase):
    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance("", "test"), 4)
        self.assertEqual(levenshtein_distance("test", ""), 4)
        self.assertEqual(levenshtein_distance("same", "same"), 0)
        self.assertEqual(levenshtein_distance("abc", "xyz"), 3)

    def test_fuzzy_search(self):
        items = ["apple", "banana", "orange", "grape", "pineapple"]

        # Test exact match
        self.assertEqual(fuzzy_search("apple", items), ["apple"])

        # Test close match
        self.assertEqual(fuzzy_search("aple", items, threshold=1), ["apple"])

        # Test multiple matches
        self.assertEqual(set(fuzzy_search("app", items, threshold=3)), {"apple", "grape"})

        # Test no match
        self.assertEqual(fuzzy_search("xyz", items, threshold=1), [])

        # Test case insensitivity
        self.assertEqual(fuzzy_search("APPLE", items, threshold=0), ["apple"])

    def test_fuzzy_search_sorting(self):
        items = ["kitten", "sitten", "sitting"]

        # 'sitten' distance 1, 'sitting' distance 3
        results = fuzzy_search("kitten", items, threshold=3)
        self.assertEqual(results, ["kitten", "sitten", "sitting"])

if __name__ == "__main__":
    unittest.main()
