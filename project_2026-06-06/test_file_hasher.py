import unittest
import os
import tempfile
import hashlib
from file_hasher import calculate_hash

class TestFileHasher(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with some content for testing
        self.test_content = b"This is a test file for hashing."

        # Create a temporary file and write the content to it
        self.fd, self.temp_file_path = tempfile.mkstemp()
        with open(self.temp_file_path, 'wb') as f:
            f.write(self.test_content)

    def tearDown(self):
        # Clean up the temporary file
        os.close(self.fd)
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_calculate_hash_sha256(self):
        expected_hash = hashlib.sha256(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.temp_file_path, 'sha256')
        self.assertEqual(expected_hash, actual_hash)

    def test_calculate_hash_md5(self):
        expected_hash = hashlib.md5(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.temp_file_path, 'md5')
        self.assertEqual(expected_hash, actual_hash)

    def test_calculate_hash_sha1(self):
        expected_hash = hashlib.sha1(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.temp_file_path, 'sha1')
        self.assertEqual(expected_hash, actual_hash)

    def test_calculate_hash_default(self):
        # Should default to sha256
        expected_hash = hashlib.sha256(self.test_content).hexdigest()
        actual_hash = calculate_hash(self.temp_file_path)
        self.assertEqual(expected_hash, actual_hash)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            calculate_hash("non_existent_file.txt")

    def test_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            calculate_hash(self.temp_file_path, 'invalid_algo')

if __name__ == '__main__':
    unittest.main()
