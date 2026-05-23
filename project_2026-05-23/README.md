# Daily Project - 2026-05-23

## Overview

Today's project is a fully functional **LRU Cache with TTL (Time-To-Live)** implemented in Python.

It combines two critical caching mechanisms into a single data structure:
1. **Least Recently Used (LRU) Eviction:** When the cache reaches its maximum capacity, the least recently accessed item is evicted to make room for new items.
2. **Time-To-Live (TTL) Expiration:** Every item stored in the cache has a specific lifespan. If an item is accessed after its TTL has expired, it is treated as non-existent and removed from the cache.

This component is useful for caching API responses, database queries, or any data that becomes stale after a certain period, while maintaining a strict memory footprint constraint.

## Features

- **O(1) Get and Put Operations:** Utilizing Python's `collections.OrderedDict`, the cache guarantees constant time operations for accessing and storing elements.
- **Lazy Expiration:** Items are removed either when they are accessed after their TTL has passed, or when they are evicted due to capacity constraints.
- **Active Cleanup:** Provides a `cleanup_expired()` utility method to proactively sweep and remove all expired items from memory.

## Usage

```python
from lru_cache import LRUCacheTTL
import time

# Create a cache with capacity of 2 items, where each item lives for 5 seconds
cache = LRUCacheTTL(capacity=2, ttl_seconds=5.0)

# Store some values
cache.put("user_1", {"name": "Alice"})
cache.put("user_2", {"name": "Bob"})

# Retrieve a value
print(cache.get("user_1")) # Output: {'name': 'Alice'}

# Exceeding capacity evicts the least recently used ("user_2" in this case, since "user_1" was just accessed)
cache.put("user_3", {"name": "Charlie"})
print(cache.get("user_2")) # Output: None

# Wait for TTL to expire
time.sleep(6)
print(cache.get("user_1")) # Output: None (Expired)
```

## Running Tests

From the repository root, run the test suite to verify the cache behavior:

```bash
PYTHONPATH=project_2026-05-23 python3 -m unittest project_2026-05-23/test_lru_cache.py
```
