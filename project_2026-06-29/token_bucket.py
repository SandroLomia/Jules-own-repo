import time
import threading

class TokenBucket:
    """
    A thread-safe Token Bucket rate limiter implementation.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initializes the Token Bucket.

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
        self.last_refill_time = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        """
        Internal method to update the number of tokens based on elapsed time.
        """
        now = time.monotonic()
        elapsed = now - self.last_refill_time

        # Calculate tokens to add based on elapsed time and refill rate
        tokens_to_add = elapsed * self.refill_rate

        # Add tokens up to the maximum capacity
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempts to consume the specified number of tokens from the bucket.

        :param tokens: Number of tokens to consume. Defaults to 1.
        :return: True if tokens were successfully consumed, False otherwise.
        """
        if tokens <= 0:
            raise ValueError("Number of tokens to consume must be greater than 0")

        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def get_tokens(self) -> float:
        """
        Returns the current number of tokens in the bucket.
        """
        with self.lock:
            self._refill()
            return self.tokens
