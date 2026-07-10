import unittest
import os
import tempfile
import shutil
from tree_generator import generate_tree

class TestTreeGenerator(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()

        # Structure:
        # test_dir/
        # ├── file1.txt
        # ├── dir1/
        # │   ├── file2.txt
        # │   └── dir2/
        # │       └── file3.txt
        # └── dir3/
        #     └── file4.txt

        open(os.path.join(self.test_dir, 'file1.txt'), 'w').close()

        os.mkdir(os.path.join(self.test_dir, 'dir1'))
        open(os.path.join(self.test_dir, 'dir1', 'file2.txt'), 'w').close()

        os.mkdir(os.path.join(self.test_dir, 'dir1', 'dir2'))
        open(os.path.join(self.test_dir, 'dir1', 'dir2', 'file3.txt'), 'w').close()

        os.mkdir(os.path.join(self.test_dir, 'dir3'))
        open(os.path.join(self.test_dir, 'dir3', 'file4.txt'), 'w').close()

        self.base_name = os.path.basename(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_generate_tree_flat(self):
        # Test full tree generation without depth limits or exclusions
        tree_str = generate_tree(self.test_dir)
        lines = tree_str.split('\n')

        self.assertEqual(lines[0], self.base_name)
        self.assertIn("├── dir1", tree_str)
        self.assertIn("│   ├── dir2", tree_str)
        self.assertIn("│   │   └── file3.txt", tree_str)
        self.assertIn("│   └── file2.txt", tree_str)
        self.assertIn("├── dir3", tree_str)
        self.assertIn("│   └── file4.txt", tree_str)
        self.assertIn("└── file1.txt", tree_str)

    def test_generate_tree_depth_limit(self):
        # Test tree generation with a depth limit of 1
        tree_str = generate_tree(self.test_dir, depth=1)

        self.assertIn("├── dir1", tree_str)
        self.assertIn("├── dir3", tree_str)
        self.assertIn("└── file1.txt", tree_str)

        # Deeper files/dirs should not be present
        self.assertNotIn("file2.txt", tree_str)
        self.assertNotIn("dir2", tree_str)
        self.assertNotIn("file3.txt", tree_str)
        self.assertNotIn("file4.txt", tree_str)

    def test_generate_tree_exclude_dirs(self):
        # Test tree generation excluding 'dir1'
        tree_str = generate_tree(self.test_dir, exclude=['dir1'])

        self.assertNotIn("dir1", tree_str)
        self.assertNotIn("file2.txt", tree_str)
        self.assertNotIn("dir2", tree_str)
        self.assertNotIn("file3.txt", tree_str)

        self.assertIn("├── dir3", tree_str)
        self.assertIn("│   └── file4.txt", tree_str)
        self.assertIn("└── file1.txt", tree_str)

if __name__ == '__main__':
    unittest.main()
