# Consistent Hashing Utility

## What is it?
This project is a Python implementation of **Consistent Hashing**, a foundational algorithmic technique used primarily in distributed systems to distribute data across multiple nodes (e.g., caches, database shards, or servers).

## Why is it useful?
In traditional modulo hashing (`hash(key) % N`), adding or removing a node drastically changes the mapping of almost all keys, leading to massive cache misses or data migrations.
Consistent hashing solves this by mapping both nodes and keys to a fixed circle (a "hash ring"). When a node is added or removed, only the keys that map to that specific node's segment of the ring are affected. This minimizes data movement and allows for elastic scaling of distributed clusters.

## How does it work?
1. **Hash Ring:** It uses a cryptographic hash function (MD5 in this case) to project both nodes and keys onto a ring of numbers.
2. **Virtual Nodes (Replicas):** To ensure a balanced distribution of keys, each physical node is hashed multiple times (default 100 replicas) to create "virtual nodes" scattered around the ring.
3. **Lookup (`O(log N)`):** It uses Python's built-in `bisect` module to quickly find the next node on the ring clockwise from the key's hash.

## Usage
```python
from consistent_hashing import ConsistentHash

# Initialize the ring with default 100 virtual nodes per real node
ch = ConsistentHash()

# Add nodes to the ring
ch.add_node("cache-server-1")
ch.add_node("cache-server-2")
ch.add_node("cache-server-3")

# Get the server a key belongs to
server = ch.get_node("user_1234_data")
print(f"Data goes to: {server}")

# Remove a node (keys will automatically map to the remaining servers)
ch.remove_node("cache-server-2")
```

## Running Tests
Run the unit tests from the repository root:
```bash
PYTHONPATH=project_2026-09-27 python3 -m unittest project_2026-09-27/test_consistent_hashing.py
```
