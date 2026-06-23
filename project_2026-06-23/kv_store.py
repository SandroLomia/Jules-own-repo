import time

class KVStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value, ttl=None):
        """Sets a key to a value with an optional TTL in seconds."""
        expiry = time.time() + ttl if ttl is not None else None
        self.store[key] = {'value': value, 'expiry': expiry}

    def get(self, key):
        """Gets the value for a key, or None if it doesn't exist or has expired."""
        if key in self.store:
            item = self.store[key]
            if item['expiry'] is None or item['expiry'] > time.time():
                return item['value']
            else:
                self.delete(key)
        return None

    def delete(self, key):
        """Deletes a key from the store."""
        if key in self.store:
            del self.store[key]

    def purge(self):
        """Removes all expired keys from the store."""
        now = time.time()
        expired_keys = [
            k for k, v in self.store.items()
            if v['expiry'] is not None and v['expiry'] <= now
        ]
        for k in expired_keys:
            self.delete(k)
