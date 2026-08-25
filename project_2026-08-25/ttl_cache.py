import time

class TTLCache:
    """
    A simple in-memory cache with Time-To-Live (TTL) for each entry.
    Values are evaluated for expiration lazily upon access.
    """
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl_seconds):
        """
        Set a value in the cache with a specified TTL in seconds.
        """
        expiry_time = time.time() + ttl_seconds
        self.cache[key] = (value, expiry_time)

    def get(self, key):
        """
        Retrieve a value from the cache. Returns None if the key doesn't exist
        or if the TTL has expired.
        """
        if key not in self.cache:
            return None

        value, expiry_time = self.cache[key]
        if time.time() > expiry_time:
            # Value has expired, lazily remove it
            del self.cache[key]
            return None

        return value

    def delete(self, key):
        """
        Delete a key from the cache.
        """
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """
        Clear all entries from the cache.
        """
        self.cache.clear()
