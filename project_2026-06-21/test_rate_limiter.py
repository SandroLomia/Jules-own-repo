import unittest
import time
from rate_limiter import TokenBucket, LeakyBucket, FixedWindow

class TestTokenBucket(unittest.TestCase):
    def test_allow_request(self):
        # 2 tokens capacity, refill 1 token per second
        limiter = TokenBucket(capacity=2, refill_rate=1.0)

        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request()) # Bucket empty

        # Wait for 1 second to refill 1 token
        time.sleep(1.0)
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

class TestLeakyBucket(unittest.TestCase):
    def test_allow_request(self):
        # 2 capacity, leak 1 request per second
        limiter = LeakyBucket(capacity=2, leak_rate=1.0)

        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request()) # Bucket full

        # Wait for 1 second to leak 1 request
        time.sleep(1.0)
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

class TestFixedWindow(unittest.TestCase):
    def test_allow_request(self):
        # Window size 1 second, max 2 requests per window
        limiter = FixedWindow(window_size=1.0, max_requests=2)

        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request()) # Max requests reached in window

        # Wait for 1 second for next window
        time.sleep(1.0)
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

if __name__ == '__main__':
    unittest.main()
