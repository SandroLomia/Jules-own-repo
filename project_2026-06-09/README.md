# Daily Project - 2026-06-09

## Overview

Today's project is a **Token Bucket Rate Limiter** utility implemented in Python.

Rate limiting is a crucial technique used in software engineering to control the rate of traffic sent or received by a network interface controller. It helps prevent abuse, manage resource usage, and ensure fair access to a service.

This implementation uses the **Token Bucket** algorithm, which works as follows:
- A "bucket" is initialized with a certain `capacity` (the maximum number of tokens it can hold).
- Tokens are added to the bucket at a constant `refill_rate` (tokens per second).
- When a request is made, we attempt to consume one or more tokens from the bucket.
- If there are enough tokens, the request is allowed (and the tokens are consumed).
- If there are not enough tokens, the request is denied (rate limited).

### Features
- Thread-safe implementation using `threading.Lock`.
- Time-based token refilling using `time.monotonic()` for precision.
- Simple, easy-to-use API.

## Usage

You can use the `TokenBucket` class in your own Python projects:

```python
import time
from rate_limiter import TokenBucket

# Initialize a bucket that holds up to 5 tokens, refilling at 1 token per second
bucket = TokenBucket(capacity=5, refill_rate=1.0)

# Consume tokens
if bucket.consume(3):
    print("Request allowed!")
else:
    print("Rate limited!")
```

### Running the Example

You can run the provided example in the file:

```bash
python3 rate_limiter.py
```

### Running the Tests

The project includes unit tests written with the built-in `unittest` framework. To run the tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-09 python3 -m unittest project_2026-06-09/test_rate_limiter.py
```
