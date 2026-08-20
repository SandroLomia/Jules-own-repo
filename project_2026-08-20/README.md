# Daily Project - 2026-08-20

## Overview

Consistent Hashing Algorithm

This project implements a Consistent Hashing algorithm in Python.

Consistent hashing is a special kind of hashing such that when a hash table is resized, only K/n keys need to be remapped on average, where K is the number of keys, and n is the number of slots. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be remapped. It is often used in distributed caching to efficiently map data objects to nodes in the system.

### How it works
The algorithm uses Python's `hashlib` to compute an MD5 hash of string representations of nodes and keys, treating the hash space as a ring. Virtual nodes (replicas) are used to ensure an even distribution of keys across the available physical nodes. Keys are assigned to the closest node moving clockwise around the ring, facilitated by Python's `bisect` module for quick lookup.

### Features
*   **Virtual Nodes (Replicas)**: Supports adding multiple replicas per node to ensure a balanced key distribution.
*   **Dynamic Scaling**: Nodes can be added and removed dynamically.
*   **Efficient Lookups**: Uses binary search to find the correct node in O(log(N)) time.

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-20 python3 -m unittest project_2026-08-20/test_consistent_hashing.py
```