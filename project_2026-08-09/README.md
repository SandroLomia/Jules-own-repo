# Daily Project - 2026-08-09

## Overview

Today's project is a Python Pomodoro Timer. It's a simple, command-line friendly utility designed for productivity and time management.

## Features

- Configurable durations for work sessions, short breaks, and long breaks (defaults: 25, 5, 15 minutes).
- Methods to trigger each session type (`start_work`, `start_short_break`, `start_long_break`).
- Simple state management.

## Usage

```python
from pomodoro import PomodoroTimer

# Initialize timer with default settings
timer = PomodoroTimer()

# Start a work session
timer.start_work()

# Start a short break
timer.start_short_break()
```

## Testing

Tests are written using the `unittest` framework and `unittest.mock.patch` to mock time so the tests run instantly.

Run the tests using:
```bash
PYTHONPATH=project_2026-08-09 python3 -m unittest project_2026-08-09/test_pomodoro.py
```
