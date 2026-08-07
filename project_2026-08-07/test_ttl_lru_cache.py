import unittest
import time
from ttl_lru_cache import TTLLRUCache

class TestTTLLRUCache(unittest.TestCase):
    def test_initialization(self):
        cache = TTLLRUCache(capacity=2, ttl=1.0)
        self.assertEqual(cache.capacity, 2)
        self.assertEqual(cache.ttl, 1.0)

        with self.assertRaises(ValueError):
            TTLLRUCache(capacity=0, ttl=1.0)
        with self.assertRaises(ValueError):
            TTLLRUCache(capacity=2, ttl=-1.0)

    def test_put_and_get(self):
        cache = TTLLRUCache(capacity=2, ttl=5.0)
        cache.put("a", 1)
        cache.put("b", 2)

        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertIsNone(cache.get("c"))

    def test_lru_eviction(self):
        cache = TTLLRUCache(capacity=2, ttl=5.0)
        cache.put("a", 1)
        cache.put("b", 2)
        # Access 'a' to make it recently used
        cache.get("a")
        # Adding 'c' should evict 'b' (least recently used)
        cache.put("c", 3)

        self.assertEqual(cache.get("a"), 1)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("c"), 3)

    def test_ttl_expiration(self):
        cache = TTLLRUCache(capacity=2, ttl=0.1) # 100ms TTL
        cache.put("a", 1)
        cache.put("b", 2)

        time.sleep(0.15) # Wait for TTL to expire

        self.assertIsNone(cache.get("a"))
        self.assertIsNone(cache.get("b"))

    def test_update_existing_key(self):
        cache = TTLLRUCache(capacity=2, ttl=5.0)
        cache.put("a", 1)
        cache.put("a", 100) # Update 'a'

        self.assertEqual(cache.get("a"), 100)
        self.assertEqual(len(cache.cache), 1)

    def test_ttl_expiration_does_not_affect_recent_items(self):
        cache = TTLLRUCache(capacity=2, ttl=0.2)
        cache.put("a", 1)
        time.sleep(0.1)

        # 'b' is put 100ms later
        cache.put("b", 2)
        time.sleep(0.15)

        # Total elapsed time > 0.25s, so 'a' should expire, but 'b' should not
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)

if __name__ == '__main__':
    unittest.main()
