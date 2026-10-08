import unittest
import tempfile
import os
import shutil
from dir_stats import get_directory_stats

class TestDirStats(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def create_file(self, filename, content):
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath

    def test_empty_directory(self):
        # Should return an empty dictionary for an empty directory
        stats = get_directory_stats(self.test_dir)
        self.assertEqual(stats, {})

    def test_single_file(self):
        self.create_file('test.txt', 'hello')  # 5 bytes
        stats = get_directory_stats(self.test_dir)
        self.assertEqual(stats, {'.txt': 5})

    def test_multiple_files_extensions(self):
        # Create some text files
        self.create_file('file1.txt', '123')     # 3 bytes
        self.create_file('file2.TXT', '45')      # 2 bytes

        # Create some python files
        self.create_file('script.py', 'print(1)') # 8 bytes

        # Create a file with no extension
        self.create_file('LICENSE', 'MIT')       # 3 bytes

        # Create a subdirectory with a file
        sub_dir = os.path.join(self.test_dir, 'sub')
        os.mkdir(sub_dir)
        with open(os.path.join(sub_dir, 'data.json'), 'w') as f:
            f.write('{}') # 2 bytes

        stats = get_directory_stats(self.test_dir)

        expected_stats = {
            '.txt': 5,
            '.py': 8,
            '': 3,
            '.json': 2
        }

        self.assertEqual(stats, expected_stats)

    def test_nonexistent_directory(self):
        # Should return an empty dictionary for a nonexistent directory
        stats = get_directory_stats(os.path.join(self.test_dir, 'does_not_exist'))
        self.assertEqual(stats, {})

if __name__ == '__main__':
    unittest.main()
