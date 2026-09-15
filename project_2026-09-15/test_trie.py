import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("apples"))

        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))

    def test_starts_with(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("appl"))
        self.assertTrue(self.trie.starts_with("apple"))
        self.assertFalse(self.trie.starts_with("apx"))
        self.assertFalse(self.trie.starts_with("apples"))

    def test_autocomplete(self):
        words = ["apple", "app", "application", "aptitude", "bat", "batman"]
        for word in words:
            self.trie.insert(word)

        # Autocomplete for "app" should return "app", "apple", "application"
        app_results = self.trie.autocomplete("app")
        self.assertEqual(set(app_results), {"app", "apple", "application"})

        # Autocomplete for "bat" should return "bat", "batman"
        bat_results = self.trie.autocomplete("bat")
        self.assertEqual(set(bat_results), {"bat", "batman"})

        # Autocomplete for "c" should return empty list
        self.assertEqual(self.trie.autocomplete("c"), [])

    def test_empty_trie(self):
        self.assertFalse(self.trie.search("anything"))
        self.assertFalse(self.trie.starts_with("any"))
        self.assertEqual(self.trie.autocomplete("a"), [])

    def test_no_match(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.search("world"))
        self.assertFalse(self.trie.starts_with("world"))
        self.assertEqual(self.trie.autocomplete("world"), [])

if __name__ == '__main__':
    unittest.main()
