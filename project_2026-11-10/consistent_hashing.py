import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas=100):
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []

    def _hash(self, key):
        """Generates an MD5 hash for the given key and returns an integer representation."""
        m = hashlib.md5()
        m.update(key.encode('utf-8'))
        return int(m.hexdigest(), 16)

    def add_node(self, node):
        """Adds a node to the hash ring with the specified number of replicas."""
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hashed_key = self._hash(replica_key)
            self.ring[hashed_key] = node
            bisect.insort(self._sorted_keys, hashed_key)

    def remove_node(self, node):
        """Removes a node and its replicas from the hash ring."""
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hashed_key = self._hash(replica_key)
            if hashed_key in self.ring:
                del self.ring[hashed_key]
                self._sorted_keys.remove(hashed_key)

    def get_node(self, key):
        """Returns the appropriate node for the given key based on the hash ring."""
        if not self.ring:
            return None

        hashed_key = self._hash(key)

        # Find the first index where the key is less than or equal to the sorted key
        index = bisect.bisect(self._sorted_keys, hashed_key)

        # If the hashed_key is greater than the largest key in the ring,
        # it wraps around to the first node in the ring.
        if index == len(self._sorted_keys):
            index = 0

        return self.ring[self._sorted_keys[index]]
