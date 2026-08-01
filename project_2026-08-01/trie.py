class TrieNode:
    """A node in the Trie data structure."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """A Trie (Prefix Tree) data structure for efficient string retrieval."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_words_with_prefix(self, prefix: str) -> list[str]:
        """Returns a list of words that start with the given prefix."""
        node = self.root
        words = []
        for char in prefix:
            if char not in node.children:
                return words
            node = node.children[char]

        self._dfs(node, prefix, words)
        return words

    def _dfs(self, node: TrieNode, prefix: str, words: list[str]) -> None:
        """Helper depth-first search to find all words from a given node."""
        if node.is_end_of_word:
            words.append(prefix)

        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, words)
