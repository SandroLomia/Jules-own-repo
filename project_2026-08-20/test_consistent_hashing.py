import unittest
from consistent_hashing import ConsistentHash

class TestConsistentHashing(unittest.TestCase):
    def test_add_and_get_node(self):
        ch = ConsistentHash(num_replicas=3)
        ch.add_node("node1")
        ch.add_node("node2")
        ch.add_node("node3")

        # Map some keys
        counts = {"node1": 0, "node2": 0, "node3": 0}
        for i in range(100):
            node = ch.get_node(f"item_{i}")
            counts[node] += 1

        self.assertEqual(sum(counts.values()), 100)
        # Check that nodes are roughly equally distributed (this test is more of a sanity check)
        self.assertTrue(all(c > 0 for c in counts.values()))

    def test_remove_node(self):
        ch = ConsistentHash(num_replicas=3)
        ch.add_node("node1")
        ch.add_node("node2")

        item = "test_item"
        node = ch.get_node(item)
        self.assertIn(node, ["node1", "node2"])

        # Remove the node that received the item
        ch.remove_node(node)

        # Re-get the item
        new_node = ch.get_node(item)
        self.assertNotEqual(node, new_node)
        self.assertIn(new_node, ["node1", "node2"])

    def test_empty_ring(self):
        ch = ConsistentHash()
        self.assertIsNone(ch.get_node("item1"))

if __name__ == '__main__':
    unittest.main()
