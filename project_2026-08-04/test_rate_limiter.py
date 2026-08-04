import unittest
import time
from rate_limiter import TokenBucketRateLimiter, SlidingWindowRateLimiter


class TestTokenBucketRateLimiter(unittest.TestCase):

    def test_allow_request_under_capacity(self):
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        # Should allow 5 requests immediately
        for _ in range(5):
            self.assertTrue(limiter.allow_request())

    def test_reject_request_over_capacity(self):
        limiter = TokenBucketRateLimiter(capacity=3, refill_rate=0.5)
        # Exhaust capacity
        for _ in range(3):
            self.assertTrue(limiter.allow_request())
        # The 4th request should be rejected as not enough time has passed
        self.assertFalse(limiter.allow_request())

    def test_refill(self):
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=10.0)
        # Exhaust capacity
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

        # Wait for refill (refill_rate is 10/s, so wait 0.1s for 1 token, 0.2s for 2 tokens)
        time.sleep(0.25)
        # Should be able to make requests again
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())


class TestSlidingWindowRateLimiter(unittest.TestCase):

    def test_allow_request_under_limit(self):
        limiter = SlidingWindowRateLimiter(limit=5, window_size=1.0)
        # Should allow 5 requests immediately
        for _ in range(5):
            self.assertTrue(limiter.allow_request())

    def test_reject_request_over_limit(self):
        limiter = SlidingWindowRateLimiter(limit=3, window_size=1.0)
        # Exhaust limit
        for _ in range(3):
            self.assertTrue(limiter.allow_request())
        # The 4th request should be rejected
        self.assertFalse(limiter.allow_request())

    def test_window_slide(self):
        limiter = SlidingWindowRateLimiter(limit=2, window_size=0.2)

        # Exhaust limit
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

        # Wait for window to slide past the old requests
        time.sleep(0.25)

        # Should be able to make requests again
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

if __name__ == '__main__':
    unittest.main()
