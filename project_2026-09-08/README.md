# Daily Project - 2026-09-08

## Overview

Today's project is a lightweight, in-memory **Key-Value Store** built in Python with Time-To-Live (TTL) support.

It was created to serve as a fast and simple caching utility.

### Features
- `set(key, value, ttl=None)`: Stores a key-value pair. Optionally provide a TTL in seconds.
- `get(key)`: Retrieves a value. If the key has expired, it is automatically removed and returns `None`.
- `delete(key)`: Removes a key manually.
- `cleanup()`: A utility method to proactively iterate through and remove all expired keys in the store, returning the count of removed keys.

### Usage

```python
from key_value_store import KeyValueStore

# Initialize the store
store = KeyValueStore()

# Store a value that never expires
store.set("permanent_key", "Some persistent data")

# Store a value that expires in 5 seconds
store.set("temporary_key", "Some temporary data", ttl=5)

# Retrieve a value
value = store.get("permanent_key")

# Clean up expired items manually
removed_count = store.cleanup()
```

### Testing

Tests are written using Python's built-in `unittest` module.

From the repository root directory, run:
```bash
PYTHONPATH=project_2026-09-08 python3 -m unittest project_2026-09-08/test_key_value_store.py
```