import unittest
import time
from kv_store import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.store = KeyValueStore()

    def test_set_and_get(self):
        self.store.set("key1", "value1")
        self.assertEqual(self.store.get("key1"), "value1")

    def test_get_nonexistent(self):
        self.assertIsNone(self.store.get("missing_key"))

    def test_ttl_expiration(self):
        self.store.set("temp_key", "temp_val", ttl=0.1)
        self.assertEqual(self.store.get("temp_key"), "temp_val")
        time.sleep(0.2)
        self.assertIsNone(self.store.get("temp_key"))

    def test_delete(self):
        self.store.set("key2", "value2")
        self.store.delete("key2")
        self.assertIsNone(self.store.get("key2"))

    def test_cleanup(self):
        self.store.set("k1", "v1", ttl=0.1)
        self.store.set("k2", "v2", ttl=0.5)
        self.store.set("k3", "v3")

        time.sleep(0.2)
        # k1 should be expired, k2 and k3 should remain
        self.store.cleanup()

        self.assertNotIn("k1", self.store._store)
        self.assertIn("k2", self.store._store)
        self.assertIn("k3", self.store._store)

if __name__ == "__main__":
    unittest.main()
