# Consistent Hashing

This project implements a **Consistent Hashing Ring**, a popular distributed systems algorithm primarily used for load balancing and data partitioning across a dynamic set of nodes (e.g., caches, database shards, or web servers).

## Purpose

In standard hashing (like `hash(key) % N`), changing the number of nodes `N` (due to a node crash or scaling up) causes nearly all keys to map to different nodes, leading to massive cache misses or data movement.

**Consistent Hashing** solves this by mapping both the nodes and the keys onto the same circular hash space (a "ring"). When a node is added or removed, only a small fraction of the keys (specifically, those adjacent to the node on the ring) are remapped.

### Virtual Nodes (Replicas)

To ensure an even distribution of keys across nodes, this implementation uses **Virtual Nodes** (or replicas). Instead of placing a physical node on the ring once, it is placed multiple times (e.g., 100 times) using different hash variants. This distributes the load more smoothly, especially when there are only a few physical nodes.

## Implementation Details

*   **Hash Function:** SHA-256 for uniform distribution.
*   **Data Structure:** A Python dictionary for O(1) hash-to-node lookups and a sorted list of keys for O(log N) nearest-neighbor searches using the `bisect` module.

## Usage

```python
from consistent_hashing import ConsistentHashRing

# Initialize the ring with some starting nodes
ring = ConsistentHashRing(["Server-A", "Server-B", "Server-C"], replicas=100)

# Get the responsible node for a given key (e.g., a user ID or session ID)
user_id = "user_12345"
server = ring.get_node(user_id)
print(f"Key '{user_id}' routes to {server}")

# Add a new node (scales up capacity)
ring.add_node("Server-D")

# Remove a failing node
ring.remove_node("Server-B")
```

## Running Tests

To run the unit tests, ensure you run them from the repository root, pointing the `PYTHONPATH` to this directory:

```bash
PYTHONPATH=project_2026-07-06 python3 -m unittest project_2026-07-06/test_consistent_hashing.py
```
