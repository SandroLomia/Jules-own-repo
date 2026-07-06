import hashlib
import bisect
from typing import List, Optional

class ConsistentHashRing:
    """
    A consistent hashing ring implementation.
    Assigns keys to nodes using a hash ring and virtual nodes (replicas)
    for better load distribution.
    """
    def __init__(self, nodes: Optional[List[str]] = None, replicas: int = 100):
        self.replicas = replicas
        self.ring: dict[int, str] = {}
        self.sorted_keys: List[int] = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key: str) -> int:
        """Generates a SHA-256 hash for a given string and returns an integer."""
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        """Adds a node (and its virtual replicas) to the hash ring."""
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hashed_key = self._hash(replica_key)
            self.ring[hashed_key] = node
            bisect.insort(self.sorted_keys, hashed_key)

    def remove_node(self, node: str) -> None:
        """Removes a node (and its virtual replicas) from the hash ring."""
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hashed_key = self._hash(replica_key)
            if hashed_key in self.ring:
                del self.ring[hashed_key]
                self.sorted_keys.remove(hashed_key)

    def get_node(self, key: str) -> Optional[str]:
        """
        Retrieves the node responsible for the given key.
        Returns None if the ring is empty.
        """
        if not self.ring:
            return None

        hashed_key = self._hash(key)

        # Find the first node on the ring with a hash >= hashed_key
        index = bisect.bisect(self.sorted_keys, hashed_key)

        # If the index is at the end, wrap around to the first node
        if index == len(self.sorted_keys):
            index = 0

        return self.ring[self.sorted_keys[index]]
