import unittest
import time
from ttl_cache import TTLCache

class TestTTLCache(unittest.TestCase):
    def setUp(self):
        self.cache = TTLCache()

    def test_set_and_get(self):
        self.cache.set("key1", "value1", ttl_seconds=10)
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_get_nonexistent(self):
        self.assertIsNone(self.cache.get("missing"))

    def test_expiration(self):
        self.cache.set("key2", "value2", ttl_seconds=0.1)
        # Should be available immediately
        self.assertEqual(self.cache.get("key2"), "value2")
        # Wait for expiration
        time.sleep(0.2)
        # Should be None after TTL has passed
        self.assertIsNone(self.cache.get("key2"))

    def test_delete(self):
        self.cache.set("key3", "value3", ttl_seconds=10)
        self.cache.delete("key3")
        self.assertIsNone(self.cache.get("key3"))

    def test_clear(self):
        self.cache.set("key4", "value4", ttl_seconds=10)
        self.cache.set("key5", "value5", ttl_seconds=10)
        self.cache.clear()
        self.assertIsNone(self.cache.get("key4"))
        self.assertIsNone(self.cache.get("key5"))
        self.assertEqual(len(self.cache.cache), 0)

if __name__ == '__main__':
    unittest.main()
