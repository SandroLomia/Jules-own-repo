import unittest
from unittest.mock import patch
from pomodoro import PomodoroTimer

class TestPomodoroTimer(unittest.TestCase):
    def setUp(self):
        self.timer = PomodoroTimer(work_duration=25, short_break=5, long_break=15)

    def test_initial_state(self):
        self.assertEqual(self.timer.state, 'IDLE')
        self.assertEqual(self.timer.work_duration, 1500)
        self.assertEqual(self.timer.short_break, 300)
        self.assertEqual(self.timer.long_break, 900)

    @patch('time.sleep')
    def test_start_work(self, mock_sleep):
        # We need to change the implementation of countdown slightly to make testing easier without taking 25 minutes
        # Since countdown runs a while loop, we will just patch time.sleep to not do anything, and check call count
        self.timer.start_work()
        self.assertEqual(mock_sleep.call_count, 1500)
        self.assertEqual(self.timer.state, 'IDLE')

    @patch('time.sleep')
    def test_start_short_break(self, mock_sleep):
        self.timer.start_short_break()
        self.assertEqual(mock_sleep.call_count, 300)
        self.assertEqual(self.timer.state, 'IDLE')

    @patch('time.sleep')
    def test_start_long_break(self, mock_sleep):
        self.timer.start_long_break()
        self.assertEqual(mock_sleep.call_count, 900)
        self.assertEqual(self.timer.state, 'IDLE')

if __name__ == '__main__':
    unittest.main()
