import unittest
import os
import shutil
import tempfile
from todo_extractor import extract_todos_from_file, scan_directory

class TestTodoExtractor(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()

        # Write test markdown files
        self.md_file1 = os.path.join(self.test_dir, "test1.md")
        with open(self.md_file1, "w") as f:
            f.write("# Project 1\n")
            f.write("- [ ] Task 1\n")
            f.write("* [ ] Task 2\n")
            f.write("- [x] Task 3\n")
            f.write("* [X] Task 4\n")
            f.write("Just some text here.\n")

        self.md_file2 = os.path.join(self.test_dir, "test2.md")
        with open(self.md_file2, "w") as f:
            f.write("# Project 2\n")
            f.write("- [ ] Nested task 1\n")
            f.write("- [ ] Nested task 2\n")

        self.txt_file = os.path.join(self.test_dir, "test.txt")
        with open(self.txt_file, "w") as f:
            f.write("- [ ] This should be ignored\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_extract_todos_from_file(self):
        pending, completed = extract_todos_from_file(self.md_file1)
        self.assertEqual(len(pending), 2)
        self.assertEqual(len(completed), 2)
        self.assertEqual(pending[0], "Task 1")
        self.assertEqual(pending[1], "Task 2")
        self.assertEqual(completed[0], "Task 3")
        self.assertEqual(completed[1], "Task 4")

    def test_scan_directory(self):
        results = scan_directory(self.test_dir)

        self.assertEqual(len(results), 2) # Should find test1.md and test2.md

        # Check test1.md
        self.assertIn(self.md_file1, results)
        self.assertEqual(len(results[self.md_file1]["pending"]), 2)
        self.assertEqual(len(results[self.md_file1]["completed"]), 2)

        # Check test2.md
        self.assertIn(self.md_file2, results)
        self.assertEqual(len(results[self.md_file2]["pending"]), 2)
        self.assertEqual(len(results[self.md_file2]["completed"]), 0)

        # Check that txt_file was ignored
        self.assertNotIn(self.txt_file, results)

if __name__ == '__main__':
    unittest.main()
