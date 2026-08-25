# Daily Project - 2026-08-25: TTLCache

## Overview

Today's project is the implementation of a **Time-To-Live (TTL) Cache** in Python. It provides a lightweight, in-memory caching mechanism where entries automatically expire after a specified duration.

## Architecture and Design

The cache is implemented in the `TTLCache` class within `ttl_cache.py`. It uses a standard Python dictionary for O(1) lookups. To efficiently manage expirations without needing a background worker thread, it uses **lazy expiration**:
- When an item is `set`, its absolute expiration time (current time + TTL) is calculated and stored alongside the value.
- When an item is accessed via `get`, the cache checks if the current time has surpassed the expiration time. If so, it removes the item and returns `None`.

## Usage

```python
from ttl_cache import TTLCache
import time

cache = TTLCache()

# Set a value with a 5-second TTL
cache.set("my_key", "my_value", ttl_seconds=5)

# Retrieve the value
print(cache.get("my_key")) # Output: "my_value"

# Wait for 6 seconds
time.sleep(6)

# The value has expired
print(cache.get("my_key")) # Output: None
```

## Running Tests

Unit tests are provided in `test_ttl_cache.py` to ensure correctness and test edge cases like immediate retrieval, expiration delays, and cache clearing.

Run the tests from the repository root:
```bash
PYTHONPATH=project_2026-08-25 python3 -m unittest project_2026-08-25/test_ttl_cache.py
```
