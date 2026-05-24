import unittest
import time
import threading
from rate_limiter import TokenBucket

class TestTokenBucket(unittest.TestCase):
    def test_initialization(self):
        bucket = TokenBucket(capacity=10, refill_rate=2.0)
        self.assertEqual(bucket.capacity, 10)
        self.assertEqual(bucket.refill_rate, 2.0)
        self.assertEqual(bucket.get_tokens(), 10.0)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            TokenBucket(capacity=0, refill_rate=1.0)
        with self.assertRaises(ValueError):
            TokenBucket(capacity=10, refill_rate=-1.0)

    def test_consume_success(self):
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        self.assertTrue(bucket.consume(3))
        self.assertAlmostEqual(bucket.get_tokens(), 2.0, delta=0.1)

    def test_consume_failure(self):
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        self.assertTrue(bucket.consume(5))
        self.assertFalse(bucket.consume(1))

    def test_refill(self):
        bucket = TokenBucket(capacity=5, refill_rate=10.0)
        # Empty the bucket
        self.assertTrue(bucket.consume(5))
        self.assertFalse(bucket.consume(1))

        # Wait for refill (10 tokens/sec -> 0.1s for 1 token)
        time.sleep(0.2)

        # We should have at least 1 token now
        self.assertTrue(bucket.consume(1))

    def test_capacity_limit(self):
        bucket = TokenBucket(capacity=5, refill_rate=10.0)

        # Consume some
        self.assertTrue(bucket.consume(2))

        # Wait enough time to over-refill
        time.sleep(0.5)

        # Tokens should be capped at capacity
        self.assertLessEqual(bucket.get_tokens(), 5.0)

    def test_thread_safety(self):
        bucket = TokenBucket(capacity=1000, refill_rate=0.1) # low refill to not interfere
        success_count = 0
        lock = threading.Lock()

        def worker():
            nonlocal success_count
            for _ in range(100):
                if bucket.consume(1):
                    with lock:
                        success_count += 1

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # 10 threads consuming 100 times = 1000 consumes attempted.
        # Max capacity is 1000, so all 1000 should succeed.
        self.assertEqual(success_count, 1000)
        self.assertAlmostEqual(bucket.get_tokens(), 0, delta=1.0)

if __name__ == '__main__':
    unittest.main()
