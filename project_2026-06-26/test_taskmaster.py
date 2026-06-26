import unittest
import os
import json
from taskmaster import add_task, list_tasks, complete_task, delete_task, load_tasks, save_tasks

class TestTaskMaster(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        # Ensure a clean state before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task_id = add_task("Test task 1", file_path=self.test_file)
        self.assertEqual(task_id, 1)
        tasks = load_tasks(file_path=self.test_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task 1")
        self.assertFalse(tasks[0]['completed'])

    def test_list_tasks(self):
        add_task("Test task 1", file_path=self.test_file)
        add_task("Test task 2", file_path=self.test_file)
        tasks = list_tasks(file_path=self.test_file)
        self.assertEqual(len(tasks), 2)

    def test_complete_task(self):
        task_id = add_task("Test task to complete", file_path=self.test_file)
        success = complete_task(task_id, file_path=self.test_file)
        self.assertTrue(success)
        tasks = load_tasks(file_path=self.test_file)
        self.assertTrue(tasks[0]['completed'])

    def test_delete_task(self):
        task_id = add_task("Test task to delete", file_path=self.test_file)
        success = delete_task(task_id, file_path=self.test_file)
        self.assertTrue(success)
        tasks = load_tasks(file_path=self.test_file)
        self.assertEqual(len(tasks), 0)

    def test_complete_nonexistent_task(self):
        success = complete_task(999, file_path=self.test_file)
        self.assertFalse(success)

    def test_delete_nonexistent_task(self):
        success = delete_task(999, file_path=self.test_file)
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
