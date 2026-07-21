# Daily Project - 2026-07-21

## Overview

Today's project is an implementation of the **Token Bucket Rate Limiter** algorithm in Python.

### What is the Token Bucket Algorithm?

The token bucket algorithm is widely used in network traffic shaping or API rate limiting. It works by checking if there are enough "tokens" in a bucket before allowing an action (like an API request) to proceed. The bucket is continuously refilled with tokens at a constant rate, up to a maximum capacity. If the bucket is full, new tokens are discarded.

This guarantees that an application can handle bursts of traffic up to the bucket's capacity, while maintaining an average rate of traffic equal to the refill rate.

### Why this algorithm?

I chose this direction today because rate limiting is a fundamental component of robust backend systems and API architectures. Implementing it from scratch using Python's `threading.Lock` and `time.monotonic()` is a great exercise in algorithmic thinking and concurrency control.

### How to use

The implementation is located in `rate_limiter.py`. You can import it and use it as follows:

```python
from rate_limiter import TokenBucket

# Create a bucket with a capacity of 100 tokens, refilling at 10 tokens per second
bucket = TokenBucket(capacity=100, refill_rate=10)

# Attempt to consume tokens (e.g., when an API request comes in)
if bucket.consume(tokens=1):
    print("Request allowed")
else:
    print("Rate limit exceeded. Try again later.")
```

### Running Tests

Unit tests are provided in `test_rate_limiter.py` covering various scenarios including successful consumption, bucket depletion, token refill over time, and thread safety.

To run the tests from the repository root:

```bash
PYTHONPATH=project_2026-07-21 python3 -m unittest project_2026-07-21/test_rate_limiter.py
```
