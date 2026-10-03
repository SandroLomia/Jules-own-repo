import unittest
import tempfile
import os
import shutil
from duplicate_finder import find_duplicates

class TestDuplicateFinder(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for tests
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def create_file(self, filename: str, content: bytes):
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(content)
        return filepath

    def test_no_duplicates(self):
        self.create_file('file1.txt', b'hello')
        self.create_file('file2.txt', b'world')
        self.create_file('file3.txt', b'testing')

        dups = find_duplicates(self.test_dir)
        self.assertEqual(len(dups), 0)

    def test_with_duplicates(self):
        self.create_file('file1.txt', b'duplicate_content')
        self.create_file('file2.txt', b'different_content')
        self.create_file('file3.txt', b'duplicate_content')

        dups = find_duplicates(self.test_dir)
        self.assertEqual(len(dups), 1)
        self.assertEqual(len(dups[0]), 2)

        # Check that the duplicated files are file1 and file3
        basenames = [os.path.basename(p) for p in dups[0]]
        self.assertIn('file1.txt', basenames)
        self.assertIn('file3.txt', basenames)
        self.assertNotIn('file2.txt', basenames)

    def test_multiple_duplicate_groups(self):
        self.create_file('groupA_1.txt', b'content_A')
        self.create_file('groupA_2.txt', b'content_A')
        self.create_file('groupA_3.txt', b'content_A')
        self.create_file('groupB_1.txt', b'content_B')
        self.create_file('groupB_2.txt', b'content_B')

        dups = find_duplicates(self.test_dir)
        self.assertEqual(len(dups), 2)

        # We don't know the order of groups, so check lengths
        lengths = sorted([len(group) for group in dups])
        self.assertEqual(lengths, [2, 3])

    def test_empty_files(self):
        # Same-sized empty files might be skipped depending on the implementation's handling of hash
        # However, they *are* identical content.
        self.create_file('empty1.txt', b'')
        self.create_file('empty2.txt', b'')
        self.create_file('empty3.txt', b'')

        dups = find_duplicates(self.test_dir)
        self.assertEqual(len(dups), 1)
        self.assertEqual(len(dups[0]), 3)

    def test_same_size_different_content(self):
        self.create_file('size5_A.txt', b'hello')
        self.create_file('size5_B.txt', b'world')

        dups = find_duplicates(self.test_dir)
        self.assertEqual(len(dups), 0)

if __name__ == '__main__':
    unittest.main()
