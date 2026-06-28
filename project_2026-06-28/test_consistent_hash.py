import unittest
from consistent_hash import ConsistentHash

class TestConsistentHash(unittest.TestCase):

    def test_empty_ring(self):
        ch = ConsistentHash()
        self.assertIsNone(ch.get_node("key1"))

    def test_single_node(self):
        ch = ConsistentHash(nodes=["node_A"], replicas=3)
        self.assertEqual(ch.get_node("key1"), "node_A")
        self.assertEqual(ch.get_node("key2"), "node_A")
        self.assertEqual(ch.get_node("key3"), "node_A")

    def test_multiple_nodes(self):
        ch = ConsistentHash(nodes=["node_A", "node_B", "node_C"], replicas=3)
        # Test that keys consistently hash to some node
        node1 = ch.get_node("user_1")
        node2 = ch.get_node("user_2")
        node3 = ch.get_node("user_3")

        self.assertIn(node1, ["node_A", "node_B", "node_C"])
        self.assertIn(node2, ["node_A", "node_B", "node_C"])
        self.assertIn(node3, ["node_A", "node_B", "node_C"])

        # Test consistency
        self.assertEqual(ch.get_node("user_1"), node1)
        self.assertEqual(ch.get_node("user_2"), node2)
        self.assertEqual(ch.get_node("user_3"), node3)

    def test_add_node(self):
        ch = ConsistentHash(nodes=["node_A", "node_B"], replicas=3)
        initial_node = ch.get_node("key_xyz")

        # Adding a node might or might not change the target for this specific key
        ch.add_node("node_C")
        new_node = ch.get_node("key_xyz")
        self.assertIn(new_node, ["node_A", "node_B", "node_C"])

    def test_remove_node(self):
        ch = ConsistentHash(nodes=["node_A", "node_B", "node_C"], replicas=3)

        # Find a key that hashes to node_B
        key_for_b = None
        for i in range(100):
            if ch.get_node(f"key_{i}") == "node_B":
                key_for_b = f"key_{i}"
                break

        if key_for_b:
            ch.remove_node("node_B")
            # Should now hash to A or C
            new_node = ch.get_node(key_for_b)
            self.assertIn(new_node, ["node_A", "node_C"])
            self.assertNotEqual(new_node, "node_B")

    def test_distribution(self):
        # A simple check to see if load is somewhat distributed across nodes.
        nodes = [f"node_{i}" for i in range(5)]
        ch = ConsistentHash(nodes=nodes, replicas=100) # Higher replicas for better distribution

        counts = {node: 0 for node in nodes}
        num_keys = 10000
        for i in range(num_keys):
            node = ch.get_node(f"key_{i}")
            counts[node] += 1

        # Expect each node to have roughly 1/5th of the keys (2000).
        # We allow a wide margin because of the randomness of md5,
        # but check that no node has 0 keys and no node has all keys.
        for node in nodes:
            self.assertGreater(counts[node], 500)
            self.assertLess(counts[node], 3500)

if __name__ == '__main__':
    unittest.main()
