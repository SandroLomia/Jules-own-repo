# Daily Project - 2026-08-01

## Overview

Today's project is a Python implementation of the **Trie (Prefix Tree)** data structure. This is highly efficient for string search operations and is commonly used in features such as autocomplete or spell checkers.

The main features of this Trie implementation include:
*   `insert(word)`: Adds a word to the trie.
*   `search(word)`: Checks if a complete word exists in the trie.
*   `starts_with(prefix)`: Checks if any word starts with a given prefix.
*   `get_words_with_prefix(prefix)`: An autocomplete feature that performs a depth-first search to find and return all stored words matching the given prefix.

## Usage

```python
from trie import Trie

# Initialize the Trie
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")
trie.insert("banana")

# Search for a word
print(trie.search("apple")) # Output: True
print(trie.search("appl"))  # Output: False

# Check for a prefix
print(trie.starts_with("app")) # Output: True

# Get autocomplete suggestions
print(trie.get_words_with_prefix("ap")) # Output: ['app', 'apple', 'apricot']
```

## Running Tests

To run the unit tests, execute the following command from the project directory:

```bash
python3 -m unittest test_trie.py
```
