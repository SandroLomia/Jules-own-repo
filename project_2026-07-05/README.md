# Daily Project - 2026-07-05: Rate Limiter Utility

## Overview
Today I implemented a **Rate Limiter Utility** in Python using the classic **Token Bucket algorithm**.

Rate limiting is an essential technique used to control the rate of traffic sent or received on a network. It can be used to prevent abuse, protect APIs from being overwhelmed, and enforce usage quotas.

## The Token Bucket Algorithm

The Token Bucket algorithm works as follows:
1. A "bucket" is given a maximum capacity of tokens.
2. Tokens are added to the bucket at a fixed rate (refill rate) up to the maximum capacity.
3. Each time a request (or function call) occurs, it attempts to consume a token from the bucket.
4. If a token is available, the request is allowed, and the token is removed.
5. If no tokens are available, the request is denied (or rate-limited).

## Features

- `TokenBucket` class: A core class handling the math and logic behind capacity, token consumption, and refilling over time.
- `@rate_limit` decorator: An easy-to-use Python decorator to wrap any function and protect it from being called too frequently.

## Usage Example

```python
from rate_limiter import rate_limit, RateLimitExceeded
import time

# Allow a maximum burst of 3 calls, regenerating 1 call per second
@rate_limit(capacity=3, refill_rate=1.0)
def process_data():
    print("Data processed!")

try:
    for _ in range(5):
        process_data()
except RateLimitExceeded as e:
    print(f"Error: {e}")
```

## Running the Tests

You can run the included unit tests using:
```bash
PYTHONPATH=. python3 -m unittest test_rate_limiter.py
```
