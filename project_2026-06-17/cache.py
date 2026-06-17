import time
from typing import Any, Optional

class TTLCache:
    def __init__(self, default_ttl: int = 60):
        self.default_ttl = default_ttl
        self.cache = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        expiration = time.time() + (ttl if ttl is not None else self.default_ttl)
        self.cache[key] = (value, expiration)

    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            value, expiration = self.cache[key]
            if time.time() <= expiration:
                return value
            else:
                del self.cache[key]
        return None

    def delete(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]

    def clear(self) -> None:
        self.cache.clear()

    def clean_up(self) -> None:
        """Removes all expired items from the cache."""
        current_time = time.time()
        keys_to_delete = [
            key for key, (_, expiration) in self.cache.items()
            if current_time > expiration
        ]
        for key in keys_to_delete:
            del self.cache[key]
