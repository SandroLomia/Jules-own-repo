import unittest
import time
from rate_limiter import TokenBucket, rate_limit, RateLimitExceeded

class TestTokenBucket(unittest.TestCase):
    def test_consume_within_capacity(self):
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        # Should be able to consume 5 tokens immediately
        for _ in range(5):
            self.assertTrue(bucket.consume(1))

    def test_consume_exceeds_capacity(self):
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        # Consume all 5
        for _ in range(5):
            self.assertTrue(bucket.consume(1))
        # 6th should fail
        self.assertFalse(bucket.consume(1))

    def test_refill_over_time(self):
        bucket = TokenBucket(capacity=2, refill_rate=10.0) # refill 10 per sec (0.1s per token)
        # Empty the bucket
        self.assertTrue(bucket.consume(1))
        self.assertTrue(bucket.consume(1))
        self.assertFalse(bucket.consume(1))

        # Wait for at least 1 token to refill (0.1 seconds)
        time.sleep(0.15)

        # Should be able to consume again
        self.assertTrue(bucket.consume(1))

    def test_max_capacity_constraint(self):
        bucket = TokenBucket(capacity=2, refill_rate=10.0)
        # Wait to ensure we'd "overfill" if there was no constraint
        time.sleep(0.3)
        # Bucket should still only have 2 tokens
        self.assertTrue(bucket.consume(1))
        self.assertTrue(bucket.consume(1))
        self.assertFalse(bucket.consume(1))

class TestRateLimitDecorator(unittest.TestCase):
    def test_decorator_allows_calls(self):
        @rate_limit(capacity=3, refill_rate=1.0)
        def my_func():
            return "success"

        # First 3 calls should succeed
        for _ in range(3):
            self.assertEqual(my_func(), "success")

    def test_decorator_blocks_calls(self):
        @rate_limit(capacity=2, refill_rate=1.0)
        def my_func():
            return "success"

        my_func()
        my_func()

        # 3rd call should raise RateLimitExceeded
        with self.assertRaises(RateLimitExceeded):
            my_func()

if __name__ == "__main__":
    unittest.main()
