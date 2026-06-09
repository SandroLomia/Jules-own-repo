import time
from threading import Lock

class TokenBucket:
    """
    A thread-safe implementation of the Token Bucket algorithm for rate limiting.
    """

    def __init__(self, capacity: int, refill_rate: float):
        """
        Initializes the Token Bucket.

        Args:
            capacity (int): The maximum number of tokens the bucket can hold.
            refill_rate (float): The rate at which tokens are added to the bucket (tokens per second).
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        if refill_rate <= 0:
            raise ValueError("Refill rate must be greater than zero.")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill_time = time.monotonic()
        self.lock = Lock()

    def _refill(self):
        """
        Refills the bucket based on the elapsed time since the last refill.
        This method must be called with the lock acquired.
        """
        now = time.monotonic()
        elapsed = now - self.last_refill_time

        # Calculate tokens to add
        tokens_to_add = elapsed * self.refill_rate

        if tokens_to_add > 0:
            self.tokens = min(float(self.capacity), self.tokens + tokens_to_add)
            self.last_refill_time = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempts to consume a specific number of tokens from the bucket.

        Args:
            tokens (int): The number of tokens to consume. Defaults to 1.

        Returns:
            bool: True if the tokens were successfully consumed, False otherwise.
        """
        if tokens <= 0:
            raise ValueError("Tokens to consume must be greater than zero.")

        if tokens > self.capacity:
            return False

        with self.lock:
            self._refill()

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            else:
                return False

    def get_tokens(self) -> float:
        """
        Returns the current number of available tokens.
        """
        with self.lock:
            self._refill()
            return self.tokens

if __name__ == "__main__":
    # Example usage
    print("Initializing Token Bucket (capacity=5, refill_rate=1 token/sec)...")
    bucket = TokenBucket(capacity=5, refill_rate=1.0)

    print(f"Tokens available: {bucket.get_tokens():.2f}")

    # Consume 3 tokens
    if bucket.consume(3):
        print("Consumed 3 tokens.")
    else:
        print("Failed to consume 3 tokens.")

    print(f"Tokens available: {bucket.get_tokens():.2f}")

    # Try to consume 3 more tokens
    if bucket.consume(3):
        print("Consumed 3 tokens.")
    else:
        print("Failed to consume 3 tokens (rate limited).")

    print("Waiting 3 seconds...")
    time.sleep(3)

    print(f"Tokens available: {bucket.get_tokens():.2f}")
    if bucket.consume(3):
        print("Consumed 3 tokens.")
    else:
        print("Failed to consume 3 tokens.")
