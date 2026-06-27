import time
from collections import OrderedDict
from typing import Any, Optional

class LRUCacheTTL:
    """
    Least Recently Used (LRU) Cache with Time-To-Live (TTL) support.
    Evicts the least recently used items when capacity is reached, and
    also lazily evicts items that have expired based on their TTL.
    """
    def __init__(self, capacity: int, default_ttl: float = 60.0):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.cache: OrderedDict[Any, tuple[Any, float]] = OrderedDict()

    def get(self, key: Any) -> Optional[Any]:
        if key not in self.cache:
            return None

        value, expiry = self.cache[key]
        if time.time() > expiry:
            # Item has expired
            del self.cache[key]
            return None

        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return value

    def put(self, key: Any, value: Any, ttl: Optional[float] = None) -> None:
        if ttl is None:
            ttl = self.default_ttl

        expiry = time.time() + ttl

        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = (value, expiry)

        if len(self.cache) > self.capacity:
            # Evict least recently used (first item)
            self.cache.popitem(last=False)

    def clear_expired(self) -> None:
        """
        Actively remove all expired items from the cache.
        """
        now = time.time()
        keys_to_delete = [k for k, v in self.cache.items() if now > v[1]]
        for k in keys_to_delete:
            del self.cache[k]

    def __len__(self) -> int:
        self.clear_expired()
        return len(self.cache)
