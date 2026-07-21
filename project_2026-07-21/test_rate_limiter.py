import unittest
import time
import threading
from rate_limiter import TokenBucket

class TestTokenBucket(unittest.TestCase):
    def test_initialization(self):
        bucket = TokenBucket(capacity=10, refill_rate=2)
        self.assertEqual(bucket.capacity, 10)
        self.assertEqual(bucket.refill_rate, 2)
        self.assertEqual(bucket.tokens, 10)

    def test_consume_success(self):
        bucket = TokenBucket(capacity=5, refill_rate=1)
        self.assertTrue(bucket.consume(1))
        self.assertTrue(bucket.consume(2))

    def test_consume_failure(self):
        bucket = TokenBucket(capacity=2, refill_rate=0.1) # very slow refill
        self.assertTrue(bucket.consume(2))
        self.assertFalse(bucket.consume(1)) # bucket should be empty

    def test_refill(self):
        bucket = TokenBucket(capacity=5, refill_rate=10) # 10 tokens per second -> 1 token per 0.1s
        self.assertTrue(bucket.consume(5))
        self.assertFalse(bucket.consume(1)) # bucket empty

        # wait enough time for at least 1 token to refill
        time.sleep(0.15)
        self.assertTrue(bucket.consume(1))
        self.assertFalse(bucket.consume(5)) # shouldn't have 5 again yet

    def test_concurrent_consumption(self):
        # We start with 10 tokens and 10 threads each trying to consume 1 token.
        # All should succeed.
        bucket = TokenBucket(capacity=10, refill_rate=1)

        results = []
        def worker():
            results.append(bucket.consume(1))

        threads = []
        for _ in range(10):
            t = threading.Thread(target=worker)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # All 10 tokens should be consumed successfully
        self.assertEqual(results.count(True), 10)

        # Next attempt should fail immediately
        self.assertFalse(bucket.consume(1))

if __name__ == '__main__':
    unittest.main()
