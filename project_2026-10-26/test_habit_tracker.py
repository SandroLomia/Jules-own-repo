import unittest
import datetime
from habit_tracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = HabitTracker()

    def test_add_habit(self):
        self.tracker.add_habit("Exercise")
        self.assertIn("Exercise", self.tracker.habits)
        self.assertEqual(self.tracker.habits["Exercise"], [])

    def test_mark_done(self):
        self.tracker.add_habit("Reading")
        # Mark done for today
        success = self.tracker.mark_done("Reading")
        self.assertTrue(success)
        today_str = datetime.date.today().isoformat()
        self.assertIn(today_str, self.tracker.habits["Reading"])

        # Mark done for a specific date
        self.tracker.mark_done("Reading", "2026-10-25")
        self.assertIn("2026-10-25", self.tracker.habits["Reading"])

        # Try to mark non-existent habit
        self.assertFalse(self.tracker.mark_done("Coding"))

        # Try invalid date format
        self.assertFalse(self.tracker.mark_done("Reading", "10-25-2026"))

    def test_get_streak(self):
        self.tracker.add_habit("Meditation")
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        two_days_ago = today - datetime.timedelta(days=2)
        three_days_ago = today - datetime.timedelta(days=3)

        # No streak initially
        self.assertEqual(self.tracker.get_streak("Meditation"), 0)

        # Streak of 1 (done yesterday, checking today)
        self.tracker.mark_done("Meditation", yesterday.isoformat())
        self.assertEqual(self.tracker.get_streak("Meditation"), 1)

        # Streak of 2 (done today and yesterday)
        self.tracker.mark_done("Meditation", today.isoformat())
        self.assertEqual(self.tracker.get_streak("Meditation"), 2)

        # Streak of 3
        self.tracker.mark_done("Meditation", two_days_ago.isoformat())
        self.assertEqual(self.tracker.get_streak("Meditation"), 3)

        # Broken streak (done 3 days ago, but not 1 or 2 days ago, checking today)
        self.tracker.add_habit("Water")
        self.tracker.mark_done("Water", three_days_ago.isoformat())
        self.assertEqual(self.tracker.get_streak("Water"), 0)

if __name__ == '__main__':
    unittest.main()
