import unittest
import time
from lru_cache import LRUCacheTTL

class TestLRUCacheTTL(unittest.TestCase):
    def test_initialization(self):
        cache = LRUCacheTTL(capacity=2, ttl_seconds=1.0)
        self.assertEqual(cache.capacity, 2)
        self.assertEqual(cache.ttl_seconds, 1.0)
        self.assertEqual(len(cache), 0)

        with self.assertRaises(ValueError):
            LRUCacheTTL(capacity=0, ttl_seconds=1.0)

        with self.assertRaises(ValueError):
            LRUCacheTTL(capacity=1, ttl_seconds=0.0)

    def test_basic_get_put(self):
        cache = LRUCacheTTL(capacity=2, ttl_seconds=10.0)
        cache.put(1, "A")
        self.assertEqual(cache.get(1), "A")
        self.assertIsNone(cache.get(2))

    def test_lru_eviction(self):
        cache = LRUCacheTTL(capacity=2, ttl_seconds=10.0)
        cache.put(1, "A")
        cache.put(2, "B")
        cache.put(3, "C") # Evicts 1

        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), "B")
        self.assertEqual(cache.get(3), "C")

    def test_lru_order_update(self):
        cache = LRUCacheTTL(capacity=2, ttl_seconds=10.0)
        cache.put(1, "A")
        cache.put(2, "B")
        cache.get(1) # 1 becomes most recently used
        cache.put(3, "C") # Evicts 2

        self.assertEqual(cache.get(1), "A")
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(3), "C")

    def test_ttl_expiration(self):
        cache = LRUCacheTTL(capacity=2, ttl_seconds=0.1)
        cache.put(1, "A")
        self.assertEqual(cache.get(1), "A")

        # Wait for expiration
        time.sleep(0.15)
        self.assertIsNone(cache.get(1))

    def test_cleanup_expired(self):
        cache = LRUCacheTTL(capacity=3, ttl_seconds=0.1)
        cache.put(1, "A")
        cache.put(2, "B")

        time.sleep(0.15)

        cache.put(3, "C") # Not expired

        cleared = cache.cleanup_expired()
        self.assertEqual(cleared, 2)
        self.assertEqual(len(cache), 1)
        self.assertEqual(cache.get(3), "C")

if __name__ == "__main__":
    unittest.main()
