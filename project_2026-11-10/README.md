# Daily Project - 2026-11-10

## Overview

Today's project is a utility for Consistent Hashing. Consistent Hashing is an algorithm used primarily in distributed systems to distribute data across a cluster of nodes. The main advantage is that when nodes are added or removed, only a small fraction of keys need to be re-mapped, unlike traditional hash tables where almost all keys would need to be moved.

## Features

- Uses MD5 hashing to map both nodes and keys onto a circular hash ring.
- Supports virtual nodes (replicas) to ensure more even distribution of keys and better load balancing.
- Handles adding and removing nodes gracefully.
- Consistently routes keys to the appropriate nodes.

## Usage

```python
from consistent_hashing import ConsistentHashRing

# Initialize the ring with a specific number of replicas per node
ring = ConsistentHashRing(replicas=100)

# Add nodes to the cluster
ring.add_node("redis-node-1")
ring.add_node("redis-node-2")
ring.add_node("redis-node-3")

# Retrieve a node for a specific key
node = ring.get_node("user:42:profile")
print(f"Key routed to: {node}")

# Remove a node
ring.remove_node("redis-node-2")
```

## Running Tests

From the root of the repository, execute:
```bash
PYTHONPATH=project_2026-11-10 python3 -m unittest project_2026-11-10/test_consistent_hashing.py
```
