import hashlib
import bisect

class ConsistentHash:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas
        self.ring = []
        self.nodes = {}

    def _hash(self, key):
        """Returns an integer hash for a given key using MD5."""
        if not isinstance(key, str):
            key = str(key)
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        """Adds a node to the hash ring with its replicas."""
        for i in range(self.num_replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            if h not in self.nodes:
                self.nodes[h] = node
                bisect.insort(self.ring, h)

    def remove_node(self, node):
        """Removes a node and its replicas from the hash ring."""
        for i in range(self.num_replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            if h in self.nodes:
                del self.nodes[h]
                self.ring.remove(h)

    def get_node(self, item):
        """Gets the appropriate node for the item."""
        if not self.ring:
            return None

        h = self._hash(item)
        idx = bisect.bisect(self.ring, h)
        if idx == len(self.ring):
            idx = 0

        return self.nodes[self.ring[idx]]
