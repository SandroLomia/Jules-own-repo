import time
import threading

class TokenBucket:
    """
    A thread-safe Token Bucket rate limiter.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: The maximum number of tokens the bucket can hold.
        :param refill_rate: The number of tokens added to the bucket per second.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be greater than 0")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        """
        Calculates how many tokens to add based on the time elapsed since the last refill.
        """
        now = time.monotonic()
        elapsed = now - self.last_refill_time
        tokens_to_add = elapsed * self.refill_rate

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Consumes the specified number of tokens from the bucket if available.

        :param tokens: The number of tokens to consume. Defaults to 1.
        :return: True if tokens were successfully consumed, False otherwise.
        """
        if tokens <= 0:
            raise ValueError("Tokens to consume must be greater than 0")

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
