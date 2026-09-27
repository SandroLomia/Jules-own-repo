import hashlib
import bisect

class ConsistentHash:
    """
    A consistent hashing implementation.
    """
    def __init__(self, num_replicas=100):
        self.num_replicas = num_replicas
        self.ring = []
        self.nodes = {}

    def _hash(self, key):
        """
        Returns a consistent hash value for a given key using MD5.
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
        m = hashlib.md5()
        m.update(key)
        return int(m.hexdigest(), 16)

    def add_node(self, node):
        """
        Adds a node to the consistent hash ring.
        """
        for i in range(self.num_replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            self.nodes[h] = node
            bisect.insort(self.ring, h)

    def remove_node(self, node):
        """
        Removes a node from the consistent hash ring.
        """
        for i in range(self.num_replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            if h in self.nodes:
                del self.nodes[h]
                self.ring.remove(h)

    def get_node(self, key):
        """
        Gets the appropriate node for a given key.
        """
        if not self.ring:
            return None

        h = self._hash(key)
        idx = bisect.bisect(self.ring, h)
        if idx == len(self.ring):
            idx = 0

        return self.nodes[self.ring[idx]]
