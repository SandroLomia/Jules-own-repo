# Daily Project - 2026-06-17

## Overview

Today's project is a robust, in-memory Time-To-Live (TTL) cache utility implemented in Python.

### Features
* Configurable default TTL (Time-To-Live).
* Set keys with an optional custom TTL overriding the default.
* Automatic invalidation of expired keys on `get`.
* Explicit `delete` and `clear` operations.
* A `clean_up` method to proactively remove expired keys and free up memory.

### Usage

```python
from cache import TTLCache
import time

# Create a cache with a default TTL of 60 seconds
my_cache = TTLCache(default_ttl=60)

# Set a value
my_cache.set("session_id", "xyz123")

# Set a value with a custom TTL (e.g., 5 seconds)
my_cache.set("temp_token", "abc987", ttl=5)

# Get a value
print(my_cache.get("session_id")) # Output: xyz123

# Wait for 6 seconds
time.sleep(6)

# The custom TTL key will be expired
print(my_cache.get("temp_token")) # Output: None

# Proactively clean up all expired keys
my_cache.clean_up()
```

### Running Tests

To run the unit tests for this utility, ensure you run it from the root of the repository to correctly set up the python path:

```bash
PYTHONPATH=project_2026-06-17 python3 -m unittest project_2026-06-17/test_cache.py
```
