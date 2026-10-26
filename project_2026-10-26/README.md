# Daily Project - 2026-10-26

## Overview

Today's project is a **Habit Tracker** in Python. It provides a simple utility class `HabitTracker` to manage daily habits, mark them as done, and calculate current streaks based on consecutive days of completion.

## Features
- **Add Habits**: Register new habits to track.
- **Mark Done**: Record the completion of a habit for a specific date (defaults to today).
- **Streak Calculation**: Calculates the current streak of consecutive days a habit has been completed. The streak continues if the habit was completed today or yesterday.

## How to use

```python
from habit_tracker import HabitTracker

tracker = HabitTracker()

# Add a habit
tracker.add_habit("Reading")

# Mark it as done today
tracker.mark_done("Reading")

# Get the current streak
streak = tracker.get_streak("Reading")
print(f"Current Reading Streak: {streak} days")
```

## Running Tests

To run the unit tests for this project, navigate to the repository root and execute:

```bash
PYTHONPATH=project_2026-10-26 python3 -m unittest project_2026-10-26/test_habit_tracker.py
```