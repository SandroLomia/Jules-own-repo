import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.trie.insert("banana")
        self.trie.insert("bat")

    def test_insert_and_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apricot"))
        self.assertTrue(self.trie.search("banana"))
        self.assertTrue(self.trie.search("bat"))

        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("batman"))
        self.assertFalse(self.trie.search("orange"))

    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertTrue(self.trie.starts_with("b"))

        self.assertFalse(self.trie.starts_with("batm"))
        self.assertFalse(self.trie.starts_with("c"))

    def test_get_words_with_prefix(self):
        words_app = self.trie.get_words_with_prefix("app")
        self.assertCountEqual(words_app, ["app", "apple"])

        words_ap = self.trie.get_words_with_prefix("ap")
        self.assertCountEqual(words_ap, ["app", "apple", "apricot"])

        words_ba = self.trie.get_words_with_prefix("ba")
        self.assertCountEqual(words_ba, ["banana", "bat"])

        words_c = self.trie.get_words_with_prefix("c")
        self.assertEqual(words_c, [])

    def test_empty_trie(self):
        empty_trie = Trie()
        self.assertFalse(empty_trie.search("hello"))
        self.assertFalse(empty_trie.starts_with("h"))
        self.assertEqual(empty_trie.get_words_with_prefix("h"), [])

        empty_trie.insert("hello")
        self.assertTrue(empty_trie.search("hello"))
        self.assertTrue(empty_trie.starts_with("h"))
        self.assertEqual(empty_trie.get_words_with_prefix("h"), ["hello"])

if __name__ == "__main__":
    unittest.main()
