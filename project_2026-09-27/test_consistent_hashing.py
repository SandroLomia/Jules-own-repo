import unittest
from consistent_hashing import ConsistentHash

class TestConsistentHashing(unittest.TestCase):
    def test_add_node(self):
        ch = ConsistentHash(num_replicas=3)
        ch.add_node("nodeA")
        self.assertEqual(len(ch.ring), 3)
        self.assertEqual(len(ch.nodes), 3)

    def test_remove_node(self):
        ch = ConsistentHash(num_replicas=3)
        ch.add_node("nodeA")
        ch.remove_node("nodeA")
        self.assertEqual(len(ch.ring), 0)
        self.assertEqual(len(ch.nodes), 0)

    def test_get_node(self):
        ch = ConsistentHash(num_replicas=100)
        ch.add_node("nodeA")
        ch.add_node("nodeB")
        ch.add_node("nodeC")

        # Consistent mapping for the same key
        node1 = ch.get_node("my_key")
        node2 = ch.get_node("my_key")
        self.assertEqual(node1, node2)

        # Ensure we get a node back
        self.assertIn(node1, ["nodeA", "nodeB", "nodeC"])

    def test_empty_ring(self):
        ch = ConsistentHash()
        self.assertIsNone(ch.get_node("some_key"))

    def test_distribution(self):
        # A basic test to see if nodes get roughly even distribution
        # Note: MD5 isn't perfectly uniform, but it should be decent over large samples
        ch = ConsistentHash(num_replicas=100)
        nodes = ["nodeA", "nodeB", "nodeC", "nodeD"]
        for node in nodes:
            ch.add_node(node)

        counts = {node: 0 for node in nodes}
        for i in range(10000):
            node = ch.get_node(f"key_{i}")
            counts[node] += 1

        # Check that every node got some keys, no one node took everything
        for node in nodes:
            self.assertGreater(counts[node], 1000)

if __name__ == '__main__':
    unittest.main()
