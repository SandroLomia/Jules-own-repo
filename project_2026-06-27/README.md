# Daily Project - 2026-06-27

## Overview

Today's project is the implementation of an **LRU Cache with TTL (Time-To-Live)** in Python.

A standard Least Recently Used (LRU) cache evicts items when it reaches its maximum capacity, starting with the items that haven't been accessed for the longest time. This implementation extends that functionality by also allowing entries to expire after a certain amount of time, known as Time-To-Live (TTL).

### Features
* **O(1) Time Complexity**: Core operations (`get` and `put`) run in average O(1) time complexity by leveraging Python's `OrderedDict`.
* **Capacity Management**: Evicts the least recently used item when inserting a new item exceeds the capacity.
* **TTL Expiration**: Supports a default TTL for the cache and custom per-item TTLs. Expired items are lazily evaluated on `get` or actively removed.
* **Length Validation**: Evaluating `len(cache)` dynamically sweeps and clears expired items to ensure the count is accurate.

### Usage Example
```python
from lru_cache import LRUCacheTTL
import time

# Create a cache with capacity 10 and default TTL of 5 seconds
cache = LRUCacheTTL(capacity=10, default_ttl=5.0)

# Put an item with the default TTL
cache.put("key1", "value1")

# Put an item with a custom TTL (2 seconds)
cache.put("key2", "value2", ttl=2.0)

# Access items (updates their position as most recently used)
print(cache.get("key1")) # Output: value1

# Wait for 3 seconds
time.sleep(3)

print(cache.get("key1")) # Output: value1 (still valid, 5s TTL)
print(cache.get("key2")) # Output: None (expired, 2s TTL)
```

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-27 python3 -m unittest project_2026-06-27/test_lru_cache.py
```
