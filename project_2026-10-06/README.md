# Daily Project - 2026-10-06

## Overview

This project implements a Least Recently Used (LRU) Cache in Python.

An LRU Cache is a cache replacement policy that discards the least recently used items first when the cache becomes full. This implementation uses `collections.OrderedDict` to achieve $O(1)$ average time complexity for both `get` and `put` operations.

## Files
- `lru_cache.py`: Contains the `LRUCache` class implementation.
- `test_lru_cache.py`: Contains `unittest` test cases to verify the correctness of the cache, including capacity eviction and updating existing keys.

## Running Tests
To run the tests for this project, navigate to the root directory of the repository and execute:

```bash
PYTHONPATH=project_2026-10-06 python3 -m unittest project_2026-10-06/test_lru_cache.py
```
