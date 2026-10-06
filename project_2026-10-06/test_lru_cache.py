import unittest
from lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_basic_put_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), -1)

    def test_eviction(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)       # 1 is now most recently used
        cache.put(3, 3)    # evicts key 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)   # updates key 1
        cache.put(3, 3)    # evicts key 2
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

if __name__ == '__main__':
    unittest.main()
