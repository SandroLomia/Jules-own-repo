import unittest
from unittest.mock import patch
import time
from rate_limiter import TokenBucket, SlidingWindowLog

class TestTokenBucket(unittest.TestCase):

    @patch('time.time')
    def test_initial_capacity(self, mock_time):
        mock_time.return_value = 1000.0
        bucket = TokenBucket(capacity=5, refill_rate=1.0)
        self.assertEqual(bucket.tokens, 5)

    @patch('time.time')
    def test_allow_request_deducts_tokens(self, mock_time):
        mock_time.return_value = 1000.0
        bucket = TokenBucket(capacity=5, refill_rate=1.0)

        self.assertTrue(bucket.allow_request(1))
        self.assertEqual(bucket.tokens, 4)

        self.assertTrue(bucket.allow_request(2))
        self.assertEqual(bucket.tokens, 2)

    @patch('time.time')
    def test_exceed_capacity(self, mock_time):
        mock_time.return_value = 1000.0
        bucket = TokenBucket(capacity=2, refill_rate=1.0)

        self.assertTrue(bucket.allow_request(1))
        self.assertTrue(bucket.allow_request(1))
        self.assertFalse(bucket.allow_request(1)) # Out of tokens
        self.assertEqual(bucket.tokens, 0)

    @patch('time.time')
    def test_refill_tokens(self, mock_time):
        mock_time.return_value = 1000.0
        bucket = TokenBucket(capacity=5, refill_rate=2.0) # Refills 2 tokens per second

        # Consume all tokens
        self.assertTrue(bucket.allow_request(5))
        self.assertEqual(bucket.tokens, 0)

        # Advance time by 1.5 seconds (should refill 3 tokens)
        mock_time.return_value = 1001.5

        # Ask for 2 tokens (should be allowed, leaving 1)
        self.assertTrue(bucket.allow_request(2))
        self.assertEqual(bucket.tokens, 1.0)

    @patch('time.time')
    def test_refill_caps_at_capacity(self, mock_time):
        mock_time.return_value = 1000.0
        bucket = TokenBucket(capacity=5, refill_rate=10.0)

        self.assertTrue(bucket.allow_request(2)) # 3 left

        # Advance time by 10 seconds (should refill 100 tokens, but cap at 5)
        mock_time.return_value = 1010.0

        self.assertTrue(bucket.allow_request(1))
        self.assertEqual(bucket.tokens, 4.0)

class TestSlidingWindowLog(unittest.TestCase):

    @patch('time.time')
    def test_requests_within_limit(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = SlidingWindowLog(window_size=10.0, max_requests=3)

        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())

        self.assertEqual(len(limiter.log), 3)

    @patch('time.time')
    def test_requests_exceed_limit(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = SlidingWindowLog(window_size=10.0, max_requests=2)

        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request()) # Exceeds limit

    @patch('time.time')
    def test_expired_requests_slide_out(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = SlidingWindowLog(window_size=5.0, max_requests=2)

        self.assertTrue(limiter.allow_request())

        mock_time.return_value = 1002.0
        self.assertTrue(limiter.allow_request())

        self.assertFalse(limiter.allow_request()) # Exceeds limit (2 requests in last 5s)

        # Advance time so the first request (at 1000.0) expires
        mock_time.return_value = 1006.0

        # The window is [1001.0, 1006.0], only the request at 1002.0 is still in the window
        # So we should be able to make 1 more request
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())

        # Check that log was pruned
        self.assertEqual(len(limiter.log), 2)
        self.assertEqual(list(limiter.log), [1002.0, 1006.0])

if __name__ == '__main__':
    unittest.main()
