# Daily Project - 2026-09-15

## Overview

Today's project is a robust implementation of a **Trie (Prefix Tree)** data structure in Python. A Trie is an efficient information retrieval data structure that is particularly well-suited for operations involving strings, such as prefix matching and autocomplete functionality.

## Features

The `Trie` class provides the following capabilities:

*   **`insert(word: str) -> None`**: Inserts a new word into the Trie. Time complexity: O(L) where L is the length of the word.
*   **`search(word: str) -> bool`**: Returns `True` if the exact word exists in the Trie, `False` otherwise. Time complexity: O(L).
*   **`starts_with(prefix: str) -> bool`**: Returns `True` if there is any previously inserted string in the Trie that has the given prefix. Time complexity: O(L) where L is the length of the prefix.
*   **`autocomplete(prefix: str) -> list[str]`**: A powerful utility that returns all words currently in the Trie that start with the given prefix. Useful for search bars or text editors. Uses Depth First Search (DFS) for fast traversal.

## Usage

```python
from trie import Trie

t = Trie()
t.insert("apple")
t.insert("application")
t.insert("aptitude")

print(t.search("apple"))          # True
print(t.starts_with("app"))       # True
print(t.autocomplete("app"))      # ['apple', 'application']
```

## Running the Tests

To ensure the Trie implementation functions correctly across various scenarios (including exact matches, prefix matches, empty states, and DFS traversal for autocomplete), a comprehensive test suite is included.

You can run the tests from the repository root using:

```bash
PYTHONPATH=project_2026-09-15 python3 -m unittest project_2026-09-15/test_trie.py
```
