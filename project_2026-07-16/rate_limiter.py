import time
import threading

class TokenBucket:
    """
    A Token Bucket rate limiter implementation.
    """
    def __init__(self, capacity: int, fill_rate: float):
        """
        Initialize the token bucket.

        :param capacity: Maximum number of tokens the bucket can hold.
        :param fill_rate: Number of tokens added to the bucket per second.
        """
        self.capacity = capacity
        self.fill_rate = float(fill_rate)
        self.tokens = float(capacity)
        self.last_update = time.time()
        self.lock = threading.Lock()

    def _add_tokens(self):
        """
        Calculate and add tokens based on elapsed time since the last update.
        Called internally before consuming tokens.
        """
        now = time.time()
        elapsed = now - self.last_update
        tokens_to_add = elapsed * self.fill_rate
        self.tokens = min(float(self.capacity), self.tokens + tokens_to_add)
        self.last_update = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempt to consume the specified number of tokens.

        :param tokens: Number of tokens to consume (default is 1).
        :return: True if successful (enough tokens available), False otherwise.
        """
        with self.lock:
            self._add_tokens()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
