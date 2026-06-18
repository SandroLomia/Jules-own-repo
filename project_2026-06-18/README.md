# Daily Project - 2026-06-18

## Overview

This project implements an O(1) Least Recently Used (LRU) Cache in Python.

### Technical Details

The LRU Cache is implemented using two main data structures:
1.  **Hash Map:** Provides O(1) lookup time to find if a key exists in the cache.
2.  **Doubly Linked List:** Provides O(1) time complexity for insertion and deletion of nodes, which is necessary to keep track of the least recently used and most recently used elements.

The `LRUCache` class initializes with a given `capacity`.
-   `get(key)`: Returns the value of the key if it exists, otherwise returns -1. It also updates the node to be the most recently used.
-   `put(key, value)`: Inserts or updates the value. If the cache reaches its capacity, it invalidates the least recently used item before inserting the new item.

### Usage

```python
from lru_cache import LRUCache

# Initialize an LRU Cache with a capacity of 2
cache = LRUCache(2)

# Insert items
cache.put(1, 1)
cache.put(2, 2)

# Retrieve item
print(cache.get(1))  # Returns 1

# Inserting a new item causes the least recently used item (key 2) to be evicted
cache.put(3, 3)
print(cache.get(2))  # Returns -1 (not found)
```

### Running Tests

To run the unit tests, use the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-06-18 python3 -m unittest project_2026-06-18/test_lru_cache.py
```
