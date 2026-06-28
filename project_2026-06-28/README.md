# Consistent Hashing

This project implements **Consistent Hashing** in Python.

## What is it?
Consistent Hashing is a fundamental algorithm used in distributed systems (such as caching layers and distributed databases) to minimize key relocation when nodes are added or removed from the system.

Unlike standard modulo-based hashing (e.g., `hash(key) % N`) where adding or removing a node changes the mapping for almost all keys, consistent hashing arranges nodes on a hash ring. A key is mapped to the first node that appears on the ring in a clockwise direction. This means only a small fraction of keys (those belonging to the modified node's segment) need to be remapped when the topology changes.

This implementation includes support for **Virtual Nodes (Replicas)**, which maps each physical node to multiple points on the hash ring. This ensures a much more balanced distribution of keys across all nodes, preventing "hotspots."

## How it works

- **MD5 Hashing**: Used to hash both nodes and keys to a 128-bit integer space.
- **Ring Data Structure**: Implemented using a sorted list of node hashes combined with Python's `bisect` module for efficient binary search O(log N) lookups.
- **Virtual Nodes**: Configurable number of replicas per physical node.

## Running Tests

To run the unit tests and verify the implementation, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-28 python3 -m unittest project_2026-06-28/test_consistent_hash.py
```
