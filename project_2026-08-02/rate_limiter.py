import time
import threading

class TokenBucketRateLimiter:
    """
    A thread-safe Token Bucket Rate Limiter algorithm implementation.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initializes the rate limiter.

        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Number of tokens added per second.
        """
        if capacity <= 0:
            raise ValueError("capacity must be strictly positive")
        if refill_rate <= 0:
            raise ValueError("refill_rate must be strictly positive")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_timestamp = time.time()
        self.lock = threading.Lock()

    def _refill(self):
        """
        Refills tokens based on the time elapsed since the last refill.
        Assumes the caller holds the lock.
        """
        now = time.time()
        elapsed_time = now - self.last_refill_timestamp

        if elapsed_time > 0:
            # Calculate the number of tokens to add
            tokens_to_add = elapsed_time * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_timestamp = now

    def consume(self, num_tokens: int = 1) -> bool:
        """
        Attempts to consume `num_tokens` from the bucket.

        :param num_tokens: Number of tokens to consume.
        :return: True if the tokens were successfully consumed, False otherwise.
        """
        if num_tokens <= 0:
            raise ValueError("num_tokens must be strictly positive")
        if num_tokens > self.capacity:
            return False # Requesting more tokens than the bucket can ever hold

        with self.lock:
            self._refill()
            if self.tokens >= num_tokens:
                self.tokens -= num_tokens
                return True
            return False
