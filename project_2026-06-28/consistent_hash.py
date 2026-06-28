import hashlib
import bisect

class ConsistentHash:
    """
    A consistent hashing implementation with virtual nodes.
    """
    def __init__(self, nodes=None, replicas=3):
        """
        Initializes the consistent hash ring.

        :param nodes: A list of initial nodes to add to the ring.
        :param replicas: The number of virtual nodes (replicas) per physical node.
        """
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """
        Generates an MD5 hash of the given key.
        """
        m = hashlib.md5()
        m.update(str(key).encode('utf-8'))
        return int(m.hexdigest(), 16)

    def add_node(self, node):
        """
        Adds a physical node to the ring, creating `replicas` virtual nodes.
        """
        for i in range(self.replicas):
            virtual_node_key = f"{node}:{i}"
            key_hash = self._hash(virtual_node_key)
            self.ring[key_hash] = node
            bisect.insort(self._sorted_keys, key_hash)

    def remove_node(self, node):
        """
        Removes a physical node and all its virtual nodes from the ring.
        """
        for i in range(self.replicas):
            virtual_node_key = f"{node}:{i}"
            key_hash = self._hash(virtual_node_key)
            if key_hash in self.ring:
                del self.ring[key_hash]
                self._sorted_keys.remove(key_hash)

    def get_node(self, string_key):
        """
        Returns the physical node responsible for the given key.
        """
        if not self.ring:
            return None

        key_hash = self._hash(string_key)

        # Find the index of the first node hash that is >= the key hash
        index = bisect.bisect_right(self._sorted_keys, key_hash)

        # If we reach the end of the ring, wrap around to the first node
        if index == len(self._sorted_keys):
            index = 0

        return self.ring[self._sorted_keys[index]]
