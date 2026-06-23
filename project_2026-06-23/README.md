# Daily Project - 2026-06-23

## Overview

Today's project is a simple, in-memory Key-Value Store implemented in Python, with support for Time-To-Live (TTL) on individual keys.

## Features

* **Set:** Store a key-value pair, with an optional TTL (in seconds).
* **Get:** Retrieve a value by key. If the key has expired, it returns `None` and lazily deletes it.
* **Delete:** Remove a key-value pair.
* **Purge:** Manually iterate through the store and remove all expired keys.

## Usage

```python
from kv_store import KVStore
import time

store = KVStore()

# Basic set and get
store.set("my_key", "my_value")
print(store.get("my_key")) # Output: my_value

# Set with TTL (1 second)
store.set("temp_key", "temp_value", ttl=1)

# Wait for 1.5 seconds
time.sleep(1.5)

# The key has expired
print(store.get("temp_key")) # Output: None
```

## Running Tests

From the root directory:

```bash
PYTHONPATH=project_2026-06-23 python3 -m unittest project_2026-06-23/test_kv_store.py
```
