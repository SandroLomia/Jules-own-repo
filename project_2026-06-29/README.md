# Token Bucket Rate Limiter

This project implements a thread-safe **Token Bucket** algorithm in Python.

## Overview

The Token Bucket algorithm is commonly used for rate limiting and traffic shaping. It works by adding tokens to a "bucket" at a constant rate. Every time a request is made or an action is performed, it "consumes" one or more tokens from the bucket.
- If there are enough tokens in the bucket, the action is allowed and tokens are removed.
- If there are not enough tokens, the action is denied (or must wait).

This allows for a steady stream of actions while also accommodating short bursts of activity, up to the maximum capacity of the bucket.

## Usage

```python
from token_bucket import TokenBucket
import time

# Create a token bucket that holds a maximum of 10 tokens
# and refills at a rate of 2 tokens per second.
bucket = TokenBucket(capacity=10, refill_rate=2.0)

# Consume tokens
if bucket.consume(1):
    print("Action allowed!")
else:
    print("Rate limit exceeded, try again later.")

# Simulate burst traffic
if bucket.consume(9):
    print("Consumed 9 tokens!")

# Now the bucket should be empty
if not bucket.consume(1):
    print("Bucket is empty!")

# Wait for tokens to refill (1 second = 2 tokens)
time.sleep(1)

# Now we can consume again
if bucket.consume(1):
    print("Token refilled and consumed!")
```

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-29 python3 -m unittest project_2026-06-29/test_token_bucket.py
```
