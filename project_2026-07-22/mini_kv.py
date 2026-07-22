import os
import json

class MiniKV:
    """
    A simple, log-structured persistent key-value store.
    """
    def __init__(self, log_file="mini_kv.log"):
        self.log_file = log_file
        self.store = {}
        self._load_from_log()

    def _load_from_log(self):
        if not os.path.exists(self.log_file):
            return
        with open(self.log_file, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    record = json.loads(line.strip())
                    action = record.get("action")
                    key = record.get("key")
                    value = record.get("value")

                    if action == "set":
                        self.store[key] = value
                    elif action == "delete":
                        self.store.pop(key, None)
                except json.JSONDecodeError:
                    pass

    def _append_to_log(self, record):
        with open(self.log_file, "a") as f:
            f.write(json.dumps(record) + "\n")

    def set(self, key, value):
        """Sets a key to a value and persists it."""
        self.store[key] = value
        self._append_to_log({"action": "set", "key": key, "value": value})

    def get(self, key, default=None):
        """Gets a value for a key, returning default if not found."""
        return self.store.get(key, default)

    def delete(self, key):
        """Deletes a key from the store and persists the deletion."""
        if key in self.store:
            del self.store[key]
            self._append_to_log({"action": "delete", "key": key})
            return True
        return False
