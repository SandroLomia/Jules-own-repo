import time

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        time_passed = now - self.last_refill_time

        # Add tokens based on time passed and refill rate
        tokens_to_add = time_passed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0.0
        self.last_leak_time = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        time_passed = now - self.last_leak_time

        # Leak water based on time passed and leak rate
        amount_to_leak = time_passed * self.leak_rate
        self.water = max(0.0, self.water - amount_to_leak)
        self.last_leak_time = now

        if self.water + 1 <= self.capacity:
            self.water += 1
            return True
        else:
            return False

class FixedWindow:
    def __init__(self, window_size: float, max_requests: int):
        self.window_size = window_size
        self.max_requests = max_requests
        self.window_start_time = time.time()
        self.request_count = 0

    def allow_request(self) -> bool:
        now = time.time()

        # Check if we are in a new window
        if now - self.window_start_time >= self.window_size:
            self.window_start_time = now
            self.request_count = 0

        if self.request_count < self.max_requests:
            self.request_count += 1
            return True
        else:
            return False
