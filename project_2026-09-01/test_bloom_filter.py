import unittest
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        # Create a Bloom filter with a capacity of 100 items and a 5% error rate
        self.bf = BloomFilter(capacity=100, error_rate=0.05)

    def test_initialization(self):
        """Test that the filter initializes with valid parameters and rejects invalid ones."""
        self.assertTrue(self.bf.size > 0)
        self.assertTrue(self.bf.hash_count > 0)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=-10, error_rate=0.05)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=100, error_rate=1.5)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=100, error_rate=0)

    def test_add_and_check(self):
        """Test adding items and checking that they are reported as possibly in the set."""
        test_items = ["apple", "banana", "cherry", "date"]

        # Initially, items should not be in the filter
        for item in test_items:
            self.assertFalse(self.bf.check(item))

        # Add items
        for item in test_items:
            self.bf.add(item)

        # Now, they must definitely report as True
        for item in test_items:
            self.assertTrue(self.bf.check(item))

    def test_non_existent_items(self):
        """Test checking items that were never added. Some might be false positives, but most should be False."""
        added_items = ["apple", "banana", "cherry", "date"]
        for item in added_items:
            self.bf.add(item)

        non_added_items = ["elephant", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine"]

        # At 5% error rate, it's highly unlikely that all of these will be false positives.
        # We can assert that at least one of them returns False (definitely not in set).
        found_false = False
        for item in non_added_items:
            if not self.bf.check(item):
                found_false = True
                break

        self.assertTrue(found_false, "Expected at least one non-added item to return False.")

if __name__ == '__main__':
    unittest.main()
