import time
from typing import Any, Optional

class TTLCache:
    """
    An in-memory key-value store with Time-To-Live (TTL) support.
    Uses lazy expiration.
    """
    def __init__(self):
        self._store = {}

    def set(self, key: Any, value: Any, ttl: Optional[float] = None) -> None:
        """
        Set a key-value pair in the cache with an optional TTL (in seconds).
        """
        expiration = time.time() + ttl if ttl is not None else None
        self._store[key] = {'value': value, 'expiration': expiration}

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve a value from the cache. Returns None if the key doesn't exist or has expired.
        """
        if key not in self._store:
            return None

        entry = self._store[key]
        if entry['expiration'] is not None and time.time() > entry['expiration']:
            # Lazy expiration: remove the expired entry
            del self._store[key]
            return None

        return entry['value']

    def delete(self, key: Any) -> None:
        """
        Remove a key from the cache.
        """
        if key in self._store:
            del self._store[key]

    def clear(self) -> None:
        """
        Clear all items from the cache.
        """
        self._store.clear()
