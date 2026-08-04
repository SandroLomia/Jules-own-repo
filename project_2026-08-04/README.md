# Daily Project - 2026-08-04: API Rate Limiters

## Overview

Today's project implements two common algorithms for API rate limiting in Python: **Token Bucket** and **Sliding Window Log**. These are designed to be thread-safe reusable components that can be integrated into web servers, API gateways, or client applications to control the rate of requests.

## Implemented Algorithms

### 1. Token Bucket Rate Limiter
The `TokenBucketRateLimiter` class allows requests based on a bucket of tokens.
- Tokens are added to the bucket at a constant `refill_rate`.
- The bucket has a maximum `capacity`.
- Each request consumes one or more tokens.
- If there are enough tokens, the request is allowed. Otherwise, it is rejected.

### 2. Sliding Window Log Rate Limiter
The `SlidingWindowRateLimiter` class keeps track of timestamps for each request.
- It maintains a queue of recent request timestamps.
- When a new request arrives, any timestamps older than the `window_size` are discarded.
- If the remaining number of timestamps is less than the `limit`, the request is allowed and its timestamp is recorded.

## Usage

```python
from rate_limiter import TokenBucketRateLimiter, SlidingWindowRateLimiter

# Token Bucket: max 10 tokens, refill 2 tokens per second
tb_limiter = TokenBucketRateLimiter(capacity=10, refill_rate=2.0)
if tb_limiter.allow_request():
    print("Token Bucket: Request allowed!")

# Sliding Window: max 5 requests per 60 seconds window
sw_limiter = SlidingWindowRateLimiter(limit=5, window_size=60.0)
if sw_limiter.allow_request():
    print("Sliding Window: Request allowed!")
```

## Running Tests

Unit tests are provided using the built-in `unittest` module. To run the tests from the root of the repository:

```bash
PYTHONPATH=project_2026-08-04 python3 -m unittest project_2026-08-04/test_rate_limiter.py
```
