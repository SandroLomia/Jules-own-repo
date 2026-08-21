# Daily Project - 2026-08-21

## Overview

Rate Limiting Algorithms

This project implements two common rate limiting algorithms in Python: **Token Bucket** and **Sliding Window Log**. These are thread-safe implementations designed to restrict the rate of operations (like API requests) to prevent abuse or system overload.

### Token Bucket
The Token Bucket algorithm adds tokens to a bucket at a fixed rate, up to a maximum capacity. Each request consumes one or more tokens. If the bucket doesn't have enough tokens, the request is denied. It allows for short bursts of traffic while maintaining a steady long-term rate.

### Sliding Window Log
The Sliding Window Log algorithm keeps a log of timestamps for each request. When a new request comes in, it removes timestamps older than the specified window size. If the number of remaining timestamps is below the allowed limit, the request is permitted and its timestamp is logged. This provides a very precise limit over a rolling time window.

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-21 python3 -m unittest project_2026-08-21/test_rate_limiter.py
```