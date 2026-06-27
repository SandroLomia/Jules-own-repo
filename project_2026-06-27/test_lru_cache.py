import unittest
import time
from lru_cache import LRUCacheTTL

class TestLRUCacheTTL(unittest.TestCase):
    def test_basic_put_get(self):
        cache = LRUCacheTTL(capacity=2)
        cache.put(1, "one")
        cache.put(2, "two")
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get(2), "two")

    def test_eviction(self):
        cache = LRUCacheTTL(capacity=2)
        cache.put(1, "one")
        cache.put(2, "two")
        # Access 1 to make it most recently used
        cache.get(1)
        cache.put(3, "three")

        # 2 should be evicted because 1 was accessed recently
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get(3), "three")

    def test_ttl_expiration(self):
        cache = LRUCacheTTL(capacity=2, default_ttl=0.1)
        cache.put(1, "one")
        self.assertEqual(cache.get(1), "one")

        # Wait for expiration
        time.sleep(0.15)
        self.assertIsNone(cache.get(1))

    def test_custom_ttl(self):
        cache = LRUCacheTTL(capacity=2, default_ttl=10.0)
        cache.put(1, "one", ttl=0.1)
        cache.put(2, "two", ttl=0.3)

        # 1 should expire first
        time.sleep(0.15)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), "two")

    def test_clear_expired(self):
        cache = LRUCacheTTL(capacity=3, default_ttl=0.1)
        cache.put(1, "one")
        cache.put(2, "two")

        time.sleep(0.15)
        cache.put(3, "three", ttl=1.0)

        self.assertEqual(len(cache), 1)
        self.assertEqual(cache.get(3), "three")

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            LRUCacheTTL(capacity=0)

if __name__ == "__main__":
    unittest.main()
