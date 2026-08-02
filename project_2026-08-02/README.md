# Daily Project - 2026-08-02

## Overview

This project implements a thread-safe **Token Bucket Rate Limiter** in Python. Rate limiting is a crucial technique in software engineering to control the rate of actions, such as API requests, to prevent abuse and ensure fair resource allocation.

### The Algorithm

The Token Bucket algorithm works as follows:
- A "bucket" is initialized with a certain `capacity` (maximum number of tokens).
- Tokens are added to the bucket at a constant `refill_rate` (tokens per second).
- If the bucket reaches its capacity, newly added tokens are discarded.
- When an action needs to be performed, it attempts to "consume" a token. If a token is available, the action is allowed. If not, the action is denied (rate limited).

## Usage

```python
from rate_limiter import TokenBucketRateLimiter
import time

# Create a rate limiter with a capacity of 5 tokens, refilling at 2 tokens per second
limiter = TokenBucketRateLimiter(capacity=5, refill_rate=2.0)

# Consume tokens
for i in range(7):
    if limiter.consume():
        print(f"Action {i} allowed")
    else:
        print(f"Action {i} rate limited")

# Wait for 1 second (should refill 2 tokens)
time.sleep(1)

if limiter.consume(2):
    print("Successfully consumed 2 tokens after waiting")
```

## Running Tests

To run the unit tests, execute the following from the root directory:
```bash
PYTHONPATH=project_2026-08-02 python3 -m unittest project_2026-08-02/test_rate_limiter.py
```
