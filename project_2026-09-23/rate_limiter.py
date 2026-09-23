import time
from typing import Dict

class TokenBucketRateLimiter:
    """
    A rate limiter implementation using the Token Bucket algorithm.
    """
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: The maximum number of tokens a bucket can hold.
        :param refill_rate: The number of tokens added to the bucket per second.
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        # Maps client_id to a dictionary containing 'tokens' and 'last_refill_time'
        self.client_buckets: Dict[str, dict] = {}

    def _refill_tokens(self, client_id: str, current_time: float):
        """
        Calculates and adds tokens to the client's bucket based on the elapsed time since the last refill.
        """
        bucket = self.client_buckets[client_id]
        time_elapsed = current_time - bucket['last_refill_time']

        # Calculate tokens to add
        tokens_to_add = time_elapsed * self.refill_rate

        # Add tokens up to the maximum capacity
        if tokens_to_add > 0:
            bucket['tokens'] = min(self.capacity, bucket['tokens'] + tokens_to_add)
            bucket['last_refill_time'] = current_time

    def allow_request(self, client_id: str) -> bool:
        """
        Determines whether a request from a client should be allowed based on available tokens.

        :param client_id: Unique identifier for the client (e.g., IP address, API key).
        :return: True if the request is allowed (token consumed), False if rate limited.
        """
        current_time = time.time()

        # Initialize bucket for new clients
        if client_id not in self.client_buckets:
            self.client_buckets[client_id] = {
                'tokens': self.capacity,
                'last_refill_time': current_time
            }

        # Refill tokens based on elapsed time
        self._refill_tokens(client_id, current_time)

        bucket = self.client_buckets[client_id]

        # Check if there are enough tokens to process the request
        if bucket['tokens'] >= 1.0:
            bucket['tokens'] -= 1.0
            return True
        else:
            return False
