import time

class KeyValueStore:
    """
    An in-memory Key-Value store with Time-To-Live (TTL) support.
    """

    def __init__(self):
        self._store = {}

    def set(self, key, value, ttl=None):
        """
        Sets a value for a given key, optionally with a TTL (in seconds).
        """
        expiration = time.time() + ttl if ttl is not None else None
        self._store[key] = {'value': value, 'expiration': expiration}

    def get(self, key):
        """
        Retrieves the value for a given key.
        Returns None if the key doesn't exist or has expired.
        """
        if key not in self._store:
            return None

        entry = self._store[key]
        if entry['expiration'] is not None and time.time() > entry['expiration']:
            del self._store[key] # Lazy expiration
            return None

        return entry['value']

    def delete(self, key):
        """
        Deletes a key-value pair from the store.
        """
        if key in self._store:
            del self._store[key]

    def cleanup(self):
        """
        Actively removes all expired keys from the store.
        """
        now = time.time()
        keys_to_delete = [
            k for k, v in self._store.items()
            if v['expiration'] is not None and now > v['expiration']
        ]
        for k in keys_to_delete:
            del self._store[k]
