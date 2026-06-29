import unittest
import time
from token_bucket import TokenBucket

class TestTokenBucket(unittest.TestCase):
    def test_initial_capacity(self):
        # Create a bucket with capacity 5, refill rate 1/sec
        bucket = TokenBucket(capacity=5, refill_rate=1.0)

        # We should be able to consume 5 tokens immediately
        self.assertTrue(bucket.consume(5))

        # Consuming 1 more token should fail, since bucket is empty
        self.assertFalse(bucket.consume(1))

    def test_consume_too_many(self):
        # Create a bucket with capacity 3, refill rate 1/sec
        bucket = TokenBucket(capacity=3, refill_rate=1.0)

        # Attempting to consume more than capacity should fail
        self.assertFalse(bucket.consume(4))

    def test_refill(self):
        # Create a bucket with capacity 2, refill rate 10/sec (0.1s per token)
        bucket = TokenBucket(capacity=2, refill_rate=10.0)

        # Empty the bucket
        self.assertTrue(bucket.consume(2))
        self.assertFalse(bucket.consume(1))

        # Wait for 0.15 seconds to allow at least 1 token to refill (1.5 tokens)
        time.sleep(0.15)

        # Now we should be able to consume 1 token
        self.assertTrue(bucket.consume(1))

        # We should not be able to consume another one yet
        self.assertFalse(bucket.consume(1))

        # Wait for another 0.15 seconds
        time.sleep(0.15)

        # Should be able to consume 1 token again
        self.assertTrue(bucket.consume(1))

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            TokenBucket(capacity=0, refill_rate=1.0)

        with self.assertRaises(ValueError):
            TokenBucket(capacity=5, refill_rate=0.0)

    def test_invalid_consume(self):
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        with self.assertRaises(ValueError):
            bucket.consume(0)

if __name__ == '__main__':
    unittest.main()
