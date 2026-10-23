import time

class KVStore:
    def __init__(self):
        self._store = {}

    def set(self, key, value, ttl_seconds=None):
        expire_at = None
        if ttl_seconds is not None:
            expire_at = time.time() + ttl_seconds

        self._store[key] = {
            'value': value,
            'expire_at': expire_at
        }

    def get(self, key):
        if key not in self._store:
            return None

        entry = self._store[key]
        if entry['expire_at'] is not None and time.time() > entry['expire_at']:
            # Key has expired, clean it up and return None
            del self._store[key]
            return None

        return entry['value']

    def delete(self, key):
        if key in self._store:
            del self._store[key]
