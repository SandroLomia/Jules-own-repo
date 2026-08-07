# TTL LRU Cache

A Python implementation of an LRU (Least Recently Used) cache with Time-To-Live (TTL) eviction.

## What is it?
This utility provides an in-memory caching mechanism that restricts the cache size while automatically expiring items after a specified amount of time. It combines the benefits of an LRU cache (preventing memory leaks by capping the number of items) with time-based eviction (preventing stale data).

## Why build it?
Many applications require caching data that changes frequently (e.g., API responses, authentication tokens, database query results). Standard LRU caches do not inherently invalidate data based on time. This `TTLLRUCache` seamlessly integrates both constraints.

## Technical Design
The `TTLLRUCache` is implemented using Python's `collections.OrderedDict`, which provides efficient `O(1)` operations for insertion, deletion, and accessing elements while maintaining insertion order.

### How it works:
1.  **Time-To-Live (TTL):** Every time an item is inserted, its insertion time is recorded. During any read operation (`get`), the cache checks if the specific requested item has expired and performs a lazy eviction if necessary.
2.  **Least Recently Used (LRU):** When the cache reaches its maximum capacity during a `put` operation, it efficiently pops the least recently used item (the first item in the `OrderedDict`) to make room for the new entry, irrespective of whether it has expired or not. Accessing an existing item via `get` moves it to the end of the `OrderedDict`, marking it as the most recently used.

## Usage

```python
import time
from ttl_lru_cache import TTLLRUCache

# Initialize a cache with a capacity of 100 items and a TTL of 60 seconds
cache = TTLLRUCache(capacity=100, ttl=60.0)

# Add items to the cache
cache.put("user_123", {"name": "Alice"})

# Retrieve items
data = cache.get("user_123")
print(data) # Output: {'name': 'Alice'}

# Expired items return None
time.sleep(61)
data = cache.get("user_123")
print(data) # Output: None
```

## Running Tests

To run the unit tests, use the following command from the root directory:
```bash
PYTHONPATH=project_2026-08-07 python3 -m unittest project_2026-08-07/test_ttl_lru_cache.py
```
