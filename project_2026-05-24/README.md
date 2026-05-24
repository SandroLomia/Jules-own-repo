# Daily Project - 2026-05-24: Token Bucket Rate Limiter

## Overview

Today's project is a robust, thread-safe implementation of the **Token Bucket** algorithm for rate limiting. Rate limiters are essential components in distributed systems and APIs to control the rate of traffic sent or received. The Token Bucket algorithm is a classic and widely used method for this purpose because it allows for bursts of traffic while enforcing a steady average rate.

### How it Works

The algorithm conceptually works like a bucket that can hold a maximum number of tokens (`capacity`). Tokens are added to the bucket at a constant rate (`refill_rate`).

*   When a request arrives, the system attempts to consume a token from the bucket.
*   If a token is available, it is consumed, and the request is processed.
*   If the bucket is empty, the request is rejected (rate limited).

### Features

*   **Thread-Safe:** Uses `threading.Lock` to ensure that multiple threads can safely attempt to consume tokens concurrently without race conditions.
*   **Continuous Refill:** Calculates the exact number of tokens to add based on the time elapsed since the last operation, providing a smooth and accurate refill rate.
*   **Zero Dependencies:** Implemented using only standard library modules (`time`, `threading`).

## Usage

```python
from rate_limiter import TokenBucket

# Create a bucket with a capacity of 10 tokens, refilling at 2 tokens per second
bucket = TokenBucket(capacity=10, refill_rate=2.0)

# Attempt to consume 1 token
if bucket.consume(1):
    print("Request processed")
else:
    print("Rate limited!")
```

## Running Tests

To run the unit tests and verify the functionality:

```bash
PYTHONPATH=project_2026-05-24 python3 -m unittest project_2026-05-24/test_rate_limiter.py
```
