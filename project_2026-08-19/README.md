# Daily Project - 2026-08-19

## Overview

**What:** An in-memory Key-Value store with Time-To-Live (TTL) support.

**Why:** To provide a lightweight caching utility for future daily projects that require temporary data storage without the overhead of an external database like Redis.

**How:** Implemented in Python using a simple dictionary to store values alongside their expiration timestamps. It features lazy expiration (checking on `get`) and an active `cleanup` method to remove expired keys. It includes full unit test coverage using the built-in `unittest` module.

## Usage

```python
from kv_store import KeyValueStore
import time

store = KeyValueStore()

# Set a key with a TTL of 2 seconds
store.set("session_token", "abc123xyz", ttl=2)

print(store.get("session_token")) # Output: abc123xyz

time.sleep(3)

print(store.get("session_token")) # Output: None (expired)
```

To run the tests:
```bash
PYTHONPATH=project_2026-08-19 python3 -m unittest project_2026-08-19/test_kv_store.py
```