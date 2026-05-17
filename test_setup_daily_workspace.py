import os
import shutil
import datetime
import tempfile
import unittest
from setup_daily_workspace import setup_workspace

class TestSetupWorkspace(unittest.TestCase):
    def setUp(self):
        # Save the original working directory
        self.original_cwd = os.getcwd()
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        # Change to the temporary directory
        os.chdir(self.test_dir)

    def tearDown(self):
        # Change back to the original working directory
        os.chdir(self.original_cwd)
        # Remove the temporary directory
        shutil.rmtree(self.test_dir)

    def test_setup_workspace_creates_directory_and_readme(self):
        setup_workspace()

        today = datetime.date.today().isoformat()
        dir_name = f"project_{today}"

        self.assertTrue(os.path.exists(dir_name))
        self.assertTrue(os.path.isdir(dir_name))

        readme_path = os.path.join(dir_name, "README.md")
        self.assertTrue(os.path.exists(readme_path))

        with open(readme_path, "r") as f:
            content = f.read()
            self.assertIn(f"# Daily Project - {today}", content)

    def test_setup_workspace_idempotent(self):
        # Run twice to make sure it handles existing directories
        setup_workspace()
        setup_workspace()

        today = datetime.date.today().isoformat()
        dir_name = f"project_{today}"
        self.assertTrue(os.path.exists(dir_name))

if __name__ == '__main__':
    unittest.main()
