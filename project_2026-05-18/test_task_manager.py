import unittest
import sqlite3
import os
import tempfile
from task_manager import init_db, add_task, list_tasks, complete_task, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary database for testing
        self.fd, self.db_path = tempfile.mkstemp(suffix=".db")
        init_db(self.db_path)

    def tearDown(self):
        os.close(self.fd)
        os.unlink(self.db_path)

    def test_add_task(self):
        task_id = add_task("Test Task", "Test Description", self.db_path)
        self.assertEqual(task_id, 1)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT title, description FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(task)
        self.assertEqual(task[0], "Test Task")
        self.assertEqual(task[1], "Test Description")

    def test_list_tasks(self):
        add_task("Task 1", db_path=self.db_path)
        add_task("Task 2", db_path=self.db_path)

        tasks = list_tasks(db_path=self.db_path)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["title"], "Task 1")
        self.assertEqual(tasks[1]["title"], "Task 2")

    def test_complete_task(self):
        task_id = add_task("Test Task", db_path=self.db_path)

        # Verify it's pending initially
        tasks = list_tasks(all_tasks=True, db_path=self.db_path)
        self.assertEqual(tasks[0]["completed"], 0)

        # Complete the task
        success = complete_task(task_id, self.db_path)
        self.assertTrue(success)

        # Verify it's completed
        tasks = list_tasks(all_tasks=True, db_path=self.db_path)
        self.assertEqual(tasks[0]["completed"], 1)

        # Verify it doesn't show in pending tasks list
        pending_tasks = list_tasks(all_tasks=False, db_path=self.db_path)
        self.assertEqual(len(pending_tasks), 0)

    def test_delete_task(self):
        task_id = add_task("Test Task", db_path=self.db_path)

        success = delete_task(task_id, self.db_path)
        self.assertTrue(success)

        tasks = list_tasks(all_tasks=True, db_path=self.db_path)
        self.assertEqual(len(tasks), 0)

    def test_complete_nonexistent_task(self):
        success = complete_task(999, self.db_path)
        self.assertFalse(success)

    def test_delete_nonexistent_task(self):
        success = delete_task(999, self.db_path)
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
