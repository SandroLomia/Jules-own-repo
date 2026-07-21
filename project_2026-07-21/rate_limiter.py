import time
import threading

class TokenBucket:
    """
    A thread-safe implementation of the Token Bucket rate limiting algorithm.
    """
    def __init__(self, capacity: float, refill_rate: float):
        """
        Initializes the Token Bucket.

        :param capacity: The maximum number of tokens the bucket can hold.
        :param refill_rate: The number of tokens added to the bucket per second.
        """
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate)
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        """
        Refills the bucket with tokens based on the time elapsed since the last refill.
        This method is expected to be called with the lock held.
        """
        now = time.monotonic()
        elapsed = now - self.last_refill

        # Calculate tokens to add
        tokens_to_add = elapsed * self.refill_rate

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempts to consume the specified number of tokens from the bucket.

        :param tokens: The number of tokens to consume.
        :return: True if the tokens were successfully consumed, False otherwise.
        """
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
