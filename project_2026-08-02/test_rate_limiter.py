import unittest
from unittest.mock import patch
from rate_limiter import TokenBucketRateLimiter

class TestTokenBucketRateLimiter(unittest.TestCase):
    def test_initialization(self):
        limiter = TokenBucketRateLimiter(capacity=10, refill_rate=2.0)
        self.assertEqual(limiter.capacity, 10)
        self.assertEqual(limiter.refill_rate, 2.0)
        self.assertEqual(limiter.tokens, 10)

        with self.assertRaises(ValueError):
            TokenBucketRateLimiter(capacity=0, refill_rate=1.0)
        with self.assertRaises(ValueError):
            TokenBucketRateLimiter(capacity=10, refill_rate=0)

    @patch('time.time')
    def test_consume_all_tokens_initially(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)

        # We start with 5 tokens
        for _ in range(5):
            self.assertTrue(limiter.consume())

        # 6th token should be rejected (no time passed)
        self.assertFalse(limiter.consume())

    @patch('time.time')
    def test_token_refill(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0) # 1 token per second

        # Consume 5 tokens
        self.assertTrue(limiter.consume(5))
        self.assertFalse(limiter.consume()) # Empty

        # Advance time by 2 seconds
        mock_time.return_value = 1002.0
        # We should now have 2 tokens
        self.assertTrue(limiter.consume(2))
        self.assertFalse(limiter.consume(1)) # Empty again

        # Advance time by 10 seconds (should cap at capacity 5)
        mock_time.return_value = 1012.0
        self.assertTrue(limiter.consume(5))
        self.assertFalse(limiter.consume(1))

    @patch('time.time')
    def test_consume_more_than_capacity(self, mock_time):
        mock_time.return_value = 1000.0
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)

        # Try to consume 6 tokens, should fail immediately without side effects
        self.assertFalse(limiter.consume(6))

        # We should still have 5 tokens
        self.assertTrue(limiter.consume(5))

    def test_invalid_consume_arguments(self):
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        with self.assertRaises(ValueError):
            limiter.consume(0)
        with self.assertRaises(ValueError):
            limiter.consume(-1)

if __name__ == '__main__':
    unittest.main()
