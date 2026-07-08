import unittest
import os
import json
import tempfile
from todo_manager import load_tasks, save_tasks, add_task, list_tasks, complete_task, delete_task

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary file to use as the database
        self.fd, self.temp_file = tempfile.mkstemp(suffix='.json')
        # Close the file descriptor so that we don't leak it;
        # the functions will open it by name
        os.close(self.fd)

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_add_task_saves_to_json(self):
        task = add_task("Buy groceries", self.temp_file)
        self.assertEqual(task['id'], 1)
        self.assertEqual(task['description'], "Buy groceries")
        self.assertFalse(task['completed'])

        # Verify the file content
        tasks = load_tasks(self.temp_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Buy groceries")

    def test_list_tasks_returns_expected_items(self):
        add_task("Task 1", self.temp_file)
        add_task("Task 2", self.temp_file)

        tasks = list_tasks(self.temp_file)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['description'], "Task 1")
        self.assertEqual(tasks[1]['description'], "Task 2")

    def test_complete_task_updates_status_to_true(self):
        task = add_task("Do laundry", self.temp_file)
        self.assertFalse(task['completed'])

        # Complete the task
        success = complete_task(task['id'], self.temp_file)
        self.assertTrue(success)

        # Verify it was updated in the file
        tasks = load_tasks(self.temp_file)
        self.assertTrue(tasks[0]['completed'])

    def test_delete_task_removes_item_from_json(self):
        task1 = add_task("Task A", self.temp_file)
        task2 = add_task("Task B", self.temp_file)

        tasks_before = load_tasks(self.temp_file)
        self.assertEqual(len(tasks_before), 2)

        # Delete the first task
        success = delete_task(task1['id'], self.temp_file)
        self.assertTrue(success)

        # Verify it was removed
        tasks_after = load_tasks(self.temp_file)
        self.assertEqual(len(tasks_after), 1)
        self.assertEqual(tasks_after[0]['id'], task2['id'])

if __name__ == '__main__':
    unittest.main()
