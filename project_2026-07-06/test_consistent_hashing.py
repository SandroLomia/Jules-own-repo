import unittest
from consistent_hashing import ConsistentHashRing

class TestConsistentHashRing(unittest.TestCase):
    def test_empty_ring(self):
        ring = ConsistentHashRing()
        self.assertIsNone(ring.get_node("any_key"))

    def test_single_node(self):
        ring = ConsistentHashRing(["nodeA"])
        self.assertEqual(ring.get_node("key1"), "nodeA")
        self.assertEqual(ring.get_node("key2"), "nodeA")

    def test_deterministic_routing(self):
        nodes = ["nodeA", "nodeB", "nodeC"]
        ring = ConsistentHashRing(nodes)

        # Keys should consistently route to the same nodes
        routing = {key: ring.get_node(key) for key in ["user123", "user456", "data789", "session000"]}

        # Even if we recreate the ring, it should route identically
        ring2 = ConsistentHashRing(nodes)
        for key, expected_node in routing.items():
            self.assertEqual(ring2.get_node(key), expected_node)

    def test_add_remove_node(self):
        ring = ConsistentHashRing(["nodeA", "nodeB"])
        # Add a node
        ring.add_node("nodeC")
        self.assertEqual(len(ring.ring), 3 * ring.replicas)
        self.assertEqual(len(ring.sorted_keys), 3 * ring.replicas)

        # Remove a node
        ring.remove_node("nodeA")
        self.assertEqual(len(ring.ring), 2 * ring.replicas)
        self.assertEqual(len(ring.sorted_keys), 2 * ring.replicas)

        # Ensure nodeA is no longer returned
        for _ in range(100):
            node = ring.get_node(f"test_key_{_}")
            self.assertNotEqual(node, "nodeA")
            self.assertIn(node, ["nodeB", "nodeC"])

    def test_distribution(self):
        # A simple check to see if load is somewhat distributed
        nodes = [f"node{i}" for i in range(5)]
        ring = ConsistentHashRing(nodes, replicas=200)

        counts = {node: 0 for node in nodes}
        for i in range(1000):
            node = ring.get_node(f"key_{i}")
            counts[node] += 1

        # Every node should ideally get some traffic
        for node, count in counts.items():
            self.assertGreater(count, 0)

if __name__ == "__main__":
    unittest.main()
