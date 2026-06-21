# Daily Project - 2026-06-21: Rate Limiter Algorithms

## Overview

This project implements three fundamental rate limiting algorithms in Python:
- **Token Bucket**: Allows bursts of traffic up to a maximum capacity, refilling tokens at a constant rate.
- **Leaky Bucket**: Processes requests at a constant rate, smoothing out bursts.
- **Fixed Window**: Limits the number of requests within a fixed time window.

## Usage

```python
from rate_limiter import TokenBucket, LeakyBucket, FixedWindow

# Token Bucket: max 10 requests, refills 2 requests per second
tb = TokenBucket(capacity=10, refill_rate=2.0)
if tb.allow_request():
    print("Request allowed")

# Leaky Bucket: max queue size 10, leaks (processes) 2 requests per second
lb = LeakyBucket(capacity=10, leak_rate=2.0)
if lb.allow_request():
    print("Request allowed")

# Fixed Window: max 5 requests per 10-second window
fw = FixedWindow(window_size=10.0, max_requests=5)
if fw.allow_request():
    print("Request allowed")
```

## Running Tests

From the repository root:
```bash
PYTHONPATH=project_2026-06-21 python3 -m unittest project_2026-06-21/test_rate_limiter.py
```
