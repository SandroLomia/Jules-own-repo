import time

class KeyValueStore:
    def __init__(self):
        self._store = {}

    def set(self, key, value, ttl=None):
        """
        Sets a key-value pair in the store.
        If ttl (Time To Live in seconds) is provided, the key will expire after ttl seconds.
        """
        expires_at = time.time() + ttl if ttl is not None else None
        self._store[key] = {'value': value, 'expires_at': expires_at}

    def get(self, key):
        """
        Retrieves the value for a given key.
        Returns None if the key does not exist or has expired.
        """
        if key not in self._store:
            return None

        entry = self._store[key]
        if entry['expires_at'] is not None and time.time() > entry['expires_at']:
            # Key has expired
            self.delete(key)
            return None

        return entry['value']

    def delete(self, key):
        """
        Deletes a key from the store if it exists.
        """
        if key in self._store:
            del self._store[key]

    def cleanup(self):
        """
        Removes all expired keys from the store.
        Returns the number of keys removed.
        """
        keys_to_delete = []
        current_time = time.time()

        for key, entry in self._store.items():
            if entry['expires_at'] is not None and current_time > entry['expires_at']:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            self.delete(key)

        return len(keys_to_delete)
