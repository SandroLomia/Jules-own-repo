# Daily Project - 2026-08-28

## Overview

This project implements `TTLCache`, an in-memory key-value store with Time-To-Live (TTL) support.

### What
A Python implementation of a caching mechanism where each entry can be assigned a time limit (TTL). Once the time limit passes, the entry is automatically considered expired and is removed when accessed.

### Why
Caching is a fundamental optimization technique. Building a custom TTL cache is an excellent way to practice working with Python dictionaries, time management, and lazy evaluation patterns. Lazy evaluation (removing an item only when it is requested and found to be expired) is much more efficient for simple caches than running a background thread to clear expired items.

### How
The `TTLCache` class uses a standard Python dictionary (`_store`) to store data.
When a value is set with a `ttl`, the expiration timestamp is calculated as `time.time() + ttl` and stored alongside the value.
When `get()` is called, the cache checks if the current `time.time()` is greater than the expiration timestamp. If so, it deletes the key and returns `None`.

## Running the Tests

To run the unit tests for the `TTLCache`, execute the following from the root directory:

```bash
PYTHONPATH=project_2026-08-28 python3 -m unittest project_2026-08-28/test_cache.py
```
