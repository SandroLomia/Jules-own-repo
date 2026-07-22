# Daily Project - 2026-07-22

## Overview

Today's project is **MiniKV**, a simple, log-structured persistent key-value store in Python.

### Features
- **In-memory dictionary** for fast lookups.
- **Log-based persistence** using JSON to append actions (set, delete) to a log file.
- **State recovery** by replaying the log file on initialization.

### Usage

```python
from mini_kv import MiniKV

# Initialize the store (will load from 'mini_kv.log' if it exists)
kv = MiniKV("my_store.log")

# Set values
kv.set("username", "jules_ai")
kv.set("theme", "dark")

# Get values
print(kv.get("username"))  # Output: jules_ai

# Delete values
kv.delete("theme")
```

### Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-07-22 python3 -m unittest project_2026-07-22/test_mini_kv.py
```
