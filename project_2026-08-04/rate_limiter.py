import time
from collections import deque
from threading import Lock
from typing import Optional


class TokenBucketRateLimiter:
    """
    A thread-safe Token Bucket rate limiter.

    Tokens are added to the bucket at a fixed rate, up to a maximum capacity.
    When a request comes in, it consumes tokens. If there are enough tokens,
    the request is allowed. Otherwise, it is rejected.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Number of tokens added to the bucket per second.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be greater than 0")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill_timestamp = time.time()
        self.lock = Lock()

    def _refill(self) -> None:
        """Refills the bucket based on the time elapsed since the last refill."""
        now = time.time()
        time_elapsed = now - self.last_refill_timestamp
        tokens_to_add = time_elapsed * self.refill_rate

        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_timestamp = now

    def allow_request(self, tokens: int = 1) -> bool:
        """
        Checks if a request consuming the given number of tokens is allowed.

        :param tokens: Number of tokens the request consumes (default 1).
        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False


class SlidingWindowRateLimiter:
    """
    A thread-safe Sliding Window log rate limiter.

    Keeps track of request timestamps in a queue. When a new request arrives,
    outdated timestamps are removed, and if the count of recent timestamps
    is within the limit, the request is allowed.
    """
    def __init__(self, limit: int, window_size: float):
        """
        :param limit: Maximum number of requests allowed in the time window.
        :param window_size: The time window size in seconds.
        """
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        if window_size <= 0:
            raise ValueError("Window size must be greater than 0")

        self.limit = limit
        self.window_size = window_size
        self.requests = deque()
        self.lock = Lock()

    def allow_request(self) -> bool:
        """
        Checks if a new request is allowed within the current sliding window.

        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            now = time.time()
            window_start = now - self.window_size

            # Remove requests older than the window
            while self.requests and self.requests[0] <= window_start:
                self.requests.popleft()

            if len(self.requests) < self.limit:
                self.requests.append(now)
                return True
            return False
