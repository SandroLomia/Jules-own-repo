import unittest
import time
from kv_store import KVStore

class TestKVStore(unittest.TestCase):
    def setUp(self):
        self.store = KVStore()

    def test_set_and_get(self):
        self.store.set('key1', 'value1')
        self.assertEqual(self.store.get('key1'), 'value1')

    def test_get_nonexistent(self):
        self.assertIsNone(self.store.get('nonexistent'))

    def test_delete(self):
        self.store.set('key1', 'value1')
        self.store.delete('key1')
        self.assertIsNone(self.store.get('key1'))

    def test_ttl_expiry(self):
        self.store.set('key1', 'value1', ttl=0.1)
        self.assertEqual(self.store.get('key1'), 'value1')
        time.sleep(0.2)
        self.assertIsNone(self.store.get('key1'))

    def test_purge(self):
        self.store.set('key1', 'value1', ttl=0.1)
        self.store.set('key2', 'value2', ttl=10)
        time.sleep(0.2)
        self.store.purge()
        self.assertNotIn('key1', self.store.store)
        self.assertIn('key2', self.store.store)

if __name__ == '__main__':
    unittest.main()
