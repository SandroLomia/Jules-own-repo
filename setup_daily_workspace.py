import os
import datetime

def setup_workspace():
    """
    Creates a new directory for today's daily project and seeds it with a README.md.
    """
    today = datetime.date.today().isoformat()
    dir_name = f"project_{today}"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Created new workspace directory: {dir_name}")

        readme_path = os.path.join(dir_name, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# Daily Project - {today}\n\n")
            f.write("## Overview\n\n")
            f.write("Describe the project built today here.\n")
        print(f"Seeded README.md in {dir_name}")
    else:
        print(f"Workspace directory {dir_name} already exists.")

if __name__ == "__main__":
    setup_workspace()
