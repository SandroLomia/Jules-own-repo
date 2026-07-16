import unittest
from unittest.mock import patch
from rate_limiter import TokenBucket
import time

class TestTokenBucket(unittest.TestCase):

    def test_initial_capacity(self):
        """Verify bucket allows consumption up to its full capacity immediately."""
        bucket = TokenBucket(capacity=5, fill_rate=1)
        # Should be able to consume 5 tokens initially
        for _ in range(5):
            self.assertTrue(bucket.consume(1))
        # 6th should fail
        self.assertFalse(bucket.consume(1))

    def test_consume_too_many(self):
        """Verify consumption fails when requesting more tokens than available."""
        bucket = TokenBucket(capacity=5, fill_rate=1)
        # Trying to consume 6 tokens from a bucket with capacity 5 should fail
        self.assertFalse(bucket.consume(6))
        # But we should still be able to consume 5
        self.assertTrue(bucket.consume(5))
        self.assertFalse(bucket.consume(1))

    def test_refill(self):
        """Verify tokens replenish correctly as time passes."""
        bucket = TokenBucket(capacity=5, fill_rate=1.0) # 1 token per second

        # Consume all 5 tokens
        self.assertTrue(bucket.consume(5))
        self.assertFalse(bucket.consume(1))

        # Simulate 2 seconds passing
        initial_time = bucket.last_update
        with patch('time.time', return_value=initial_time + 2.0):
            # Should now have 2 tokens, enough for 2 requests
            self.assertTrue(bucket.consume(2))
            self.assertFalse(bucket.consume(1))

    def test_max_capacity(self):
        """Verify the bucket never exceeds its maximum capacity even after a long time."""
        bucket = TokenBucket(capacity=5, fill_rate=10.0) # 10 tokens per sec

        # Consume 2 tokens, 3 left
        self.assertTrue(bucket.consume(2))

        # Simulate 10 seconds passing (would add 100 tokens)
        initial_time = bucket.last_update
        with patch('time.time', return_value=initial_time + 10.0):
            # Try to consume 6 tokens (which is > capacity 5). Should fail.
            self.assertFalse(bucket.consume(6))
            # But we can consume 5 (the max capacity)
            self.assertTrue(bucket.consume(5))
            self.assertFalse(bucket.consume(1))

if __name__ == '__main__':
    unittest.main()
