import time
from collections import OrderedDict
from typing import Any, Optional

class LRUCacheTTL:
    """
    A Least Recently Used (LRU) Cache with Time-to-Live (TTL) expiration.
    Provides O(1) time complexity for get and put operations.
    Evicts the least recently used item when capacity is reached.
    Evicts items that have lived past their TTL.
    """
    def __init__(self, capacity: int, ttl_seconds: float):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        if ttl_seconds <= 0:
            raise ValueError("TTL must be greater than 0")

        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self.cache: OrderedDict[Any, tuple[Any, float]] = OrderedDict()

    def get(self, key: Any) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache and has not expired.
        Returns None if key doesn't exist or has expired.
        """
        if key not in self.cache:
            return None

        value, timestamp = self.cache[key]

        # Check if expired
        if time.time() - timestamp > self.ttl_seconds:
            # Item expired, remove it
            del self.cache[key]
            return None

        # Move to end to mark as most recently used
        self.cache.move_to_end(key)
        return value

    def put(self, key: Any, value: Any) -> None:
        """
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation,
        evict the least recently used key.
        """
        # If key exists, we overwrite and update its freshness
        if key in self.cache:
            del self.cache[key]

        # Add new key-value with current timestamp
        self.cache[key] = (value, time.time())

        # Check capacity
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

    def cleanup_expired(self) -> int:
        """
        Utility method to proactively clear all expired items.
        Returns the number of items cleared.
        """
        current_time = time.time()
        expired_keys = []

        for key, (_, timestamp) in self.cache.items():
            if current_time - timestamp > self.ttl_seconds:
                expired_keys.append(key)

        for key in expired_keys:
            del self.cache[key]

        return len(expired_keys)

    def __len__(self) -> int:
        return len(self.cache)
