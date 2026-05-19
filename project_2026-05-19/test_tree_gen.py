import unittest
import os
import shutil
import tempfile
from tree_gen import generate_tree

class TestTreeGen(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()

        # Structure:
        # test_dir/
        # ├── dir1/
        # │   ├── file1.txt
        # │   └── file2.txt
        # ├── dir2/
        # │   └── subdir1/
        # │       └── file3.txt
        # └── root_file.txt

        os.makedirs(os.path.join(self.test_dir, "dir1"))
        os.makedirs(os.path.join(self.test_dir, "dir2", "subdir1"))

        with open(os.path.join(self.test_dir, "root_file.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(self.test_dir, "dir1", "file1.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(self.test_dir, "dir1", "file2.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(self.test_dir, "dir2", "subdir1", "file3.txt"), "w") as f:
            f.write("test")

    def tearDown(self):
        # Remove the temporary directory after tests
        shutil.rmtree(self.test_dir)

    def test_basic_tree_generation(self):
        tree = generate_tree(self.test_dir)

        # Directories are sorted first, then files.
        expected_lines = [
            "├── dir1",
            "│   ├── file1.txt",
            "│   └── file2.txt",
            "├── dir2",
            "│   └── subdir1",
            "│       └── file3.txt",
            "└── root_file.txt"
        ]

        actual_lines = [line for line in tree.split("\n") if line.strip()]
        self.assertEqual(actual_lines, expected_lines)

    def test_max_depth_0(self):
        # max_depth=0 means it shouldn't show the contents inside the subdirectories
        tree = generate_tree(self.test_dir, max_depth=0)

        expected_lines = [
            "├── dir1",
            "├── dir2",
            "└── root_file.txt"
        ]

        actual_lines = [line for line in tree.split("\n") if line.strip()]
        self.assertEqual(actual_lines, expected_lines)

    def test_max_depth_1(self):
        # max_depth=1 means it should show contents of dir1 and dir2, but not subdir1's contents
        tree = generate_tree(self.test_dir, max_depth=1)

        expected_lines = [
            "├── dir1",
            "│   ├── file1.txt",
            "│   └── file2.txt",
            "├── dir2",
            "│   └── subdir1",
            "└── root_file.txt"
        ]

        actual_lines = [line for line in tree.split("\n") if line.strip()]
        self.assertEqual(actual_lines, expected_lines)

    def test_ignore_dirs(self):
        tree = generate_tree(self.test_dir, ignore_dirs=["dir1"])

        expected_lines = [
            "├── dir2",
            "│   └── subdir1",
            "│       └── file3.txt",
            "└── root_file.txt"
        ]

        actual_lines = [line for line in tree.split("\n") if line.strip()]
        self.assertEqual(actual_lines, expected_lines)

if __name__ == '__main__':
    unittest.main()
