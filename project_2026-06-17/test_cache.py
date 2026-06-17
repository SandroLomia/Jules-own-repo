import unittest
import time
from cache import TTLCache

class TestTTLCache(unittest.TestCase):
    def setUp(self):
        self.cache = TTLCache(default_ttl=1)

    def test_set_and_get(self):
        self.cache.set("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_get_expired(self):
        self.cache.set("key1", "value1", ttl=0.1)
        time.sleep(0.2)
        self.assertIsNone(self.cache.get("key1"))

    def test_delete(self):
        self.cache.set("key1", "value1")
        self.cache.delete("key1")
        self.assertIsNone(self.cache.get("key1"))

    def test_clear(self):
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.clear()
        self.assertIsNone(self.cache.get("key1"))
        self.assertIsNone(self.cache.get("key2"))

    def test_clean_up(self):
        self.cache.set("key1", "value1", ttl=0.1)
        self.cache.set("key2", "value2", ttl=10)
        time.sleep(0.2)
        self.cache.clean_up()
        self.assertNotIn("key1", self.cache.cache)
        self.assertIn("key2", self.cache.cache)

if __name__ == '__main__':
    unittest.main()
