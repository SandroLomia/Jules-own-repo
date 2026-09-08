import unittest
import time
from key_value_store import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.store = KeyValueStore()

    def test_set_and_get(self):
        self.store.set("key1", "value1")
        self.assertEqual(self.store.get("key1"), "value1")

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.store.get("nonexistent"))

    def test_ttl_expiration(self):
        # Set a key with 0.1 second TTL
        self.store.set("key_ttl", "value2", ttl=0.1)
        self.assertEqual(self.store.get("key_ttl"), "value2")

        # Wait for TTL to expire
        time.sleep(0.15)
        self.assertIsNone(self.store.get("key_ttl"))

        # Verify it was removed from internal store
        self.assertNotIn("key_ttl", self.store._store)

    def test_delete(self):
        self.store.set("key3", "value3")
        self.store.delete("key3")
        self.assertIsNone(self.store.get("key3"))

    def test_cleanup(self):
        self.store.set("key_keep", "value4")
        self.store.set("key_expire1", "value5", ttl=0.1)
        self.store.set("key_expire2", "value6", ttl=0.1)

        # Wait for TTLs to expire
        time.sleep(0.15)

        # Cleanup should remove the 2 expired keys
        removed_count = self.store.cleanup()
        self.assertEqual(removed_count, 2)

        # Check internal store
        self.assertIn("key_keep", self.store._store)
        self.assertNotIn("key_expire1", self.store._store)
        self.assertNotIn("key_expire2", self.store._store)

if __name__ == '__main__':
    unittest.main()
