import unittest
import time
from cache import TTLCache

class TestTTLCache(unittest.TestCase):
    def setUp(self):
        self.cache = TTLCache()

    def test_set_and_get_no_ttl(self):
        self.cache.set("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.cache.get("nonexistent"))

    def test_set_with_ttl_not_expired(self):
        self.cache.set("key2", "value2", ttl=1.0)
        # Should be available immediately
        self.assertEqual(self.cache.get("key2"), "value2")

    def test_set_with_ttl_expired(self):
        self.cache.set("key3", "value3", ttl=0.1)
        time.sleep(0.15) # Wait for it to expire
        self.assertIsNone(self.cache.get("key3"))

    def test_overwrite_key(self):
        self.cache.set("key4", "value4")
        self.assertEqual(self.cache.get("key4"), "value4")

        # Overwrite with new value and no TTL
        self.cache.set("key4", "new_value")
        self.assertEqual(self.cache.get("key4"), "new_value")

    def test_delete_key(self):
        self.cache.set("key5", "value5")
        self.cache.delete("key5")
        self.assertIsNone(self.cache.get("key5"))

        # Deleting non-existent key should not raise error
        self.cache.delete("nonexistent_key")

    def test_clear_cache(self):
        self.cache.set("k1", "v1")
        self.cache.set("k2", "v2")
        self.cache.clear()

        self.assertIsNone(self.cache.get("k1"))
        self.assertIsNone(self.cache.get("k2"))

if __name__ == '__main__':
    unittest.main()
