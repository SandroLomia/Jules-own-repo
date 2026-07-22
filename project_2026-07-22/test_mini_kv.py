import unittest
import os
from mini_kv import MiniKV

class TestMiniKV(unittest.TestCase):
    def setUp(self):
        self.test_log_file = "test_mini_kv.log"
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
        self.kv = MiniKV(self.test_log_file)

    def tearDown(self):
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

    def test_set_and_get(self):
        self.kv.set("name", "Alice")
        self.assertEqual(self.kv.get("name"), "Alice")
        self.assertIsNone(self.kv.get("nonexistent"))
        self.assertEqual(self.kv.get("nonexistent", "default_val"), "default_val")

    def test_delete(self):
        self.kv.set("age", 30)
        self.assertTrue(self.kv.delete("age"))
        self.assertIsNone(self.kv.get("age"))
        self.assertFalse(self.kv.delete("nonexistent"))

    def test_persistence(self):
        self.kv.set("city", "New York")
        self.kv.set("country", "USA")
        self.kv.delete("city")

        # Load from the same log file in a new instance
        kv2 = MiniKV(self.test_log_file)
        self.assertIsNone(kv2.get("city"))
        self.assertEqual(kv2.get("country"), "USA")

if __name__ == '__main__':
    unittest.main()
