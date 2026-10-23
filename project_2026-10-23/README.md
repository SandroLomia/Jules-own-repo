# Daily Project - 2026-10-23

## Overview

Today's project is a simple, lightweight In-Memory Key-Value Store with Time-To-Live (TTL) support written in Python.

### Features
* **Set**: Add or update key-value pairs with an optional TTL (in seconds).
* **Get**: Retrieve the value for a given key. Automatically handles expiration, returning `None` if the key has expired.
* **Delete**: Remove a key from the store.

### Usage Example

```python
from kv_store import KVStore
import time

store = KVStore()

# Basic usage
store.set("greeting", "Hello World!")
print(store.get("greeting")) # Output: Hello World!

# Usage with TTL
store.set("temp_key", "I will disappear", ttl_seconds=2)
print(store.get("temp_key")) # Output: I will disappear

time.sleep(2.1)
print(store.get("temp_key")) # Output: None

# Delete
store.set("another", "value")
store.delete("another")
print(store.get("another")) # Output: None
```

### Running Tests
To run the tests for this project from the root directory of the repository:
```bash
PYTHONPATH=project_2026-10-23 python3 -m unittest project_2026-10-23/test_kv_store.py
```