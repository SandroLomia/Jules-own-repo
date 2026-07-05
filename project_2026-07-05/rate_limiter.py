import time
from functools import wraps

class RateLimitExceeded(Exception):
    """Exception raised when the rate limit is exceeded."""
    pass

class TokenBucket:
    """
    A simple implementation of the Token Bucket algorithm for rate limiting.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Number of tokens added per second.
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill_timestamp = time.monotonic()

    def _refill(self):
        """Refills the bucket based on the time elapsed since the last refill."""
        now = time.monotonic()
        time_elapsed = now - self.last_refill_timestamp
        tokens_to_add = time_elapsed * self.refill_rate

        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_timestamp = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempts to consume the specified number of tokens from the bucket.
        Returns True if successful, False if there are not enough tokens.
        """
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

def rate_limit(capacity: int, refill_rate: float):
    """
    A decorator that applies a rate limit to a function using a Token Bucket.

    :param capacity: Maximum number of calls allowed in a burst.
    :param refill_rate: The rate at which the capacity is replenished (calls per second).
    """
    bucket = TokenBucket(capacity, refill_rate)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not bucket.consume(1):
                raise RateLimitExceeded(f"Rate limit exceeded. Capacity: {capacity}, Refill Rate: {refill_rate}/s")
            return func(*args, **kwargs)
        return wrapper
    return decorator
