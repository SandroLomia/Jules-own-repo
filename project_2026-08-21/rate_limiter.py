import time
from collections import deque
from threading import Lock

class TokenBucket:
    """
    Token Bucket rate limiting algorithm.
    Tokens are added at a fixed rate. Requests are allowed if there are enough tokens.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Number of tokens added per second.
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.lock = Lock()

    def allow_request(self, tokens: int = 1) -> bool:
        """
        Check if a request can be allowed and deduct tokens.
        :param tokens: Number of tokens required for the request.
        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            now = time.time()
            time_elapsed = now - self.last_refill_time

            # Refill tokens
            tokens_to_add = time_elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

class SlidingWindowLog:
    """
    Sliding Window Log rate limiting algorithm.
    Maintains a log of timestamps for each request. Logs older than the window size are discarded.
    """
    def __init__(self, window_size: float, max_requests: int):
        """
        :param window_size: Size of the time window in seconds.
        :param max_requests: Maximum number of requests allowed in the window.
        """
        self.window_size = window_size
        self.max_requests = max_requests
        self.log = deque()
        self.lock = Lock()

    def allow_request(self) -> bool:
        """
        Check if a request can be allowed.
        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            now = time.time()

            # Remove outdated requests
            while self.log and self.log[0] <= now - self.window_size:
                self.log.popleft()

            if len(self.log) < self.max_requests:
                self.log.append(now)
                return True
            return False
