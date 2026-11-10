import unittest
from consistent_hashing import ConsistentHashRing

class TestConsistentHashRing(unittest.TestCase):

    def setUp(self):
        self.ring = ConsistentHashRing(replicas=3)

    def test_add_node_adds_replicas(self):
        self.ring.add_node("nodeA")
        self.assertEqual(len(self.ring.ring), 3)
        self.assertEqual(len(self.ring._sorted_keys), 3)

        # Verify nodeA is the value for all keys
        for node in self.ring.ring.values():
            self.assertEqual(node, "nodeA")

    def test_remove_node_removes_replicas(self):
        self.ring.add_node("nodeA")
        self.ring.add_node("nodeB")

        self.assertEqual(len(self.ring.ring), 6)

        self.ring.remove_node("nodeA")

        self.assertEqual(len(self.ring.ring), 3)
        self.assertEqual(len(self.ring._sorted_keys), 3)

        # Verify only nodeB is left
        for node in self.ring.ring.values():
            self.assertEqual(node, "nodeB")

    def test_get_node_routes_keys_consistently(self):
        nodes = ["nodeA", "nodeB", "nodeC"]
        for node in nodes:
            self.ring.add_node(node)

        key1 = "user:123"
        key2 = "user:456"
        key3 = "user:789"

        node_for_key1 = self.ring.get_node(key1)
        node_for_key2 = self.ring.get_node(key2)
        node_for_key3 = self.ring.get_node(key3)

        # Ensure it always returns the same node for the same key
        self.assertEqual(self.ring.get_node(key1), node_for_key1)
        self.assertEqual(self.ring.get_node(key2), node_for_key2)
        self.assertEqual(self.ring.get_node(key3), node_for_key3)

    def test_get_node_empty_ring_returns_none(self):
        empty_ring = ConsistentHashRing()
        self.assertIsNone(empty_ring.get_node("any_key"))

if __name__ == "__main__":
    unittest.main()
