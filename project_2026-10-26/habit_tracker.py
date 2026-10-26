import datetime

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit_name):
        """Adds a new habit to track."""
        if habit_name not in self.habits:
            self.habits[habit_name] = []
        return True

    def mark_done(self, habit_name, date_str=None):
        """Marks a habit as done for a specific date (YYYY-MM-DD). Defaults to today."""
        if habit_name not in self.habits:
            return False

        if date_str is None:
            date_str = datetime.date.today().isoformat()

        # Ensure the date string is valid
        try:
            datetime.date.fromisoformat(date_str)
        except ValueError:
            return False

        if date_str not in self.habits[habit_name]:
            self.habits[habit_name].append(date_str)
            # keep it sorted
            self.habits[habit_name].sort()
        return True

    def get_streak(self, habit_name, today_str=None):
        """Calculates the current streak for a given habit."""
        if habit_name not in self.habits or not self.habits[habit_name]:
            return 0

        if today_str is None:
            today = datetime.date.today()
        else:
            try:
                 today = datetime.date.fromisoformat(today_str)
            except ValueError:
                 return 0

        dates = [datetime.date.fromisoformat(d) for d in self.habits[habit_name]]

        streak = 0
        current_date = today

        # Check if they did it today or yesterday to continue a streak
        if dates and (dates[-1] == today or dates[-1] == today - datetime.timedelta(days=1)):

             # If they haven't done it today but did it yesterday, we start checking from yesterday
             if dates[-1] != today:
                 current_date = today - datetime.timedelta(days=1)
                 streak = 1
             else:
                 streak = 1

             # Work backwards to find consecutive days
             for i in range(len(dates) - 2, -1, -1):
                expected_date = current_date - datetime.timedelta(days=1)
                if dates[i] == expected_date:
                    streak += 1
                    current_date = expected_date
                else:
                    break

        return streak
