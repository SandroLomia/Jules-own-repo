import unittest
import time
from unittest.mock import patch
from rate_limiter import TokenBucketRateLimiter

class TestTokenBucketRateLimiter(unittest.TestCase):

    def setUp(self):
        # Capacity of 5 tokens, refilling at 1 token per second
        self.limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
        self.client_id = "test_client"

    def test_allow_requests_within_capacity(self):
        # Initially, the bucket should have 5 tokens, allowing 5 consecutive requests
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(self.client_id))

    def test_reject_requests_when_capacity_exhausted(self):
        # Consume all 5 tokens
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(self.client_id))

        # The 6th request should be rejected as the bucket is empty
        self.assertFalse(self.limiter.allow_request(self.client_id))

    @patch('time.time')
    def test_refill_tokens_over_time(self, mock_time):
        mock_time.return_value = 100.0  # Start time

        # Consume 5 tokens
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(self.client_id))

        # The next one fails immediately
        self.assertFalse(self.limiter.allow_request(self.client_id))

        # Advance time by 2.5 seconds (should refill 2.5 tokens)
        mock_time.return_value = 102.5

        # We can make 2 more requests
        self.assertTrue(self.limiter.allow_request(self.client_id))
        self.assertTrue(self.limiter.allow_request(self.client_id))

        # The 3rd request should fail (0.5 tokens remaining)
        self.assertFalse(self.limiter.allow_request(self.client_id))

    @patch('time.time')
    def test_capacity_limit(self, mock_time):
        mock_time.return_value = 100.0

        # Consume 1 token, leaving 4
        self.assertTrue(self.limiter.allow_request(self.client_id))

        # Advance time by 10 seconds (should try to add 10 tokens)
        mock_time.return_value = 110.0

        # Even after 10s, bucket capacity shouldn't exceed 5
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(self.client_id))

        # 6th should fail
        self.assertFalse(self.limiter.allow_request(self.client_id))

    def test_multiple_clients_independent(self):
        client_a = "client_a"
        client_b = "client_b"

        # Consume all tokens for client_a
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(client_a))

        self.assertFalse(self.limiter.allow_request(client_a))

        # client_b should still have all 5 tokens available
        for _ in range(5):
            self.assertTrue(self.limiter.allow_request(client_b))

if __name__ == '__main__':
    unittest.main()
