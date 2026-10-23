import unittest
import time
from kv_store import KVStore

class TestKVStore(unittest.TestCase):
    def setUp(self):
        self.store = KVStore()

    def test_set_and_get_basic(self):
        self.store.set("foo", "bar")
        self.assertEqual(self.store.get("foo"), "bar")

    def test_get_nonexistent(self):
        self.assertIsNone(self.store.get("nonexistent"))

    def test_ttl_expiration(self):
        self.store.set("foo", "bar", ttl_seconds=0.1)
        self.assertEqual(self.store.get("foo"), "bar")
        time.sleep(0.2)
        self.assertIsNone(self.store.get("foo"))

    def test_overwrite_value(self):
        self.store.set("foo", "bar")
        self.assertEqual(self.store.get("foo"), "bar")

        self.store.set("foo", "baz")
        self.assertEqual(self.store.get("foo"), "baz")

    def test_overwrite_value_with_ttl(self):
        self.store.set("foo", "bar", ttl_seconds=0.1)
        self.assertEqual(self.store.get("foo"), "bar")

        self.store.set("foo", "baz", ttl_seconds=1.0)
        time.sleep(0.2)
        # Should not be expired because it was overwritten with longer TTL
        self.assertEqual(self.store.get("foo"), "baz")

    def test_delete(self):
        self.store.set("foo", "bar")
        self.assertEqual(self.store.get("foo"), "bar")
        self.store.delete("foo")
        self.assertIsNone(self.store.get("foo"))

if __name__ == '__main__':
    unittest.main()
