import time
from collections import OrderedDict

class TTLLRUCache:
    """
    An LRU (Least Recently Used) cache with Time-To-Live (TTL) eviction.
    """
    def __init__(self, capacity: int, ttl: float):
        """
        Initializes the TTLLRUCache.

        :param capacity: The maximum number of items the cache can hold.
        :param ttl: The time-to-live for cache items, in seconds.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        if ttl <= 0:
            raise ValueError("TTL must be greater than 0")

        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieves a value from the cache if it exists and hasn't expired.
        Uses lazy eviction for expired items.

        :param key: The key to look up.
        :return: The cached value, or None if the key doesn't exist or has expired.
        """
        if key not in self.cache:
            return None

        value, timestamp = self.cache[key]
        if time.time() - timestamp > self.ttl:
            # Lazy eviction: remove expired item on access
            del self.cache[key]
            return None

        # Move to end to mark as most recently used
        self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        """
        Adds or updates a value in the cache with the current timestamp.

        :param key: The key for the item.
        :param value: The value to store.
        """
        if key in self.cache:
            # Update existing entry and move to end
            self.cache[key] = (value, time.time())
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Cache is full, pop the first item (least recently used)
                # It might be expired, which is fine, we just evict it anyway.
                self.cache.popitem(last=False)
            self.cache[key] = (value, time.time())
