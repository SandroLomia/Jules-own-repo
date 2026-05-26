import unittest
import os
import hashlib
from file_hasher import calculate_hash

class TestFileHasher(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_filepath = "test_file.txt"
        self.test_content = b"Hello, world! This is a test file for hashing."
        with open(self.test_filepath, "wb") as f:
            f.write(self.test_content)

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)

    def test_md5_hash(self):
        expected_hash = hashlib.md5(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.test_filepath, "md5")
        self.assertEqual(actual_hash, expected_hash)

    def test_sha1_hash(self):
        expected_hash = hashlib.sha1(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.test_filepath, "sha1")
        self.assertEqual(actual_hash, expected_hash)

    def test_sha256_hash(self):
        expected_hash = hashlib.sha256(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.test_filepath, "sha256")
        self.assertEqual(actual_hash, expected_hash)

    def test_default_algorithm(self):
        # The default algorithm is sha256
        expected_hash = hashlib.sha256(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.test_filepath)
        self.assertEqual(actual_hash, expected_hash)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            calculate_hash("non_existent_file.txt")

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            calculate_hash(self.test_filepath, "unsupported_algo_xyz")

if __name__ == '__main__':
    unittest.main()
