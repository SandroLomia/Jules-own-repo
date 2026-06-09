import unittest
import time
from rate_limiter import TokenBucket

class TestTokenBucket(unittest.TestCase):

    def test_initialization(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        self.assertEqual(bucket.capacity, 10)
        self.assertEqual(bucket.refill_rate, 2.0)
        self.assertAlmostEqual(bucket.get_tokens(), 10.0, places=2)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            TokenBucket(capacity=0, refill_rate=1.0)
        with self.assertRaises(ValueError):
            TokenBucket(capacity=10, refill_rate=0.0)
        with self.assertRaises(ValueError):
            TokenBucket(capacity=-5, refill_rate=1.0)

    def test_consume_valid(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        self.assertTrue(bucket.consume(5))
        self.assertAlmostEqual(bucket.get_tokens(), 5.0, places=1)

    def test_consume_too_many(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        self.assertFalse(bucket.consume(15))
        self.assertAlmostEqual(bucket.get_tokens(), 10.0, places=1)

    def test_consume_invalid_amount(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        with self.assertRaises(ValueError):
            bucket.consume(0)
        with self.assertRaises(ValueError):
            bucket.consume(-2)

    def test_refill(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        # Consume all tokens
        self.assertTrue(bucket.consume(10))
        self.assertAlmostEqual(bucket.get_tokens(), 0.0, places=1)

        # Wait 1 second, should get 2 tokens
        time.sleep(1)
        self.assertTrue(bucket.consume(2))

        # Another wait, should get limited if we ask for 3 after 1 sec
        time.sleep(1)
        self.assertFalse(bucket.consume(3))

    def test_capacity_limit(self):
        bucket = TokenBucket(capacity=5, refill_rate=10.0)
        self.assertTrue(bucket.consume(5))
        # Wait enough time to refill more than capacity
        time.sleep(1)
        self.assertAlmostEqual(bucket.get_tokens(), 5.0, places=1)

if __name__ == '__main__':
    unittest.main()
