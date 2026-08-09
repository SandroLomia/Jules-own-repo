import time

class PomodoroTimer:
    def __init__(self, work_duration=25, short_break=5, long_break=15):
        self.work_duration = work_duration * 60
        self.short_break = short_break * 60
        self.long_break = long_break * 60
        self.state = 'IDLE'

    def start_work(self):
        self.state = 'WORK'
        self._countdown(self.work_duration)
        self.state = 'IDLE'

    def start_short_break(self):
        self.state = 'SHORT_BREAK'
        self._countdown(self.short_break)
        self.state = 'IDLE'

    def start_long_break(self):
        self.state = 'LONG_BREAK'
        self._countdown(self.long_break)
        self.state = 'IDLE'

    def _countdown(self, seconds):
        while seconds > 0:
            time.sleep(1)
            seconds -= 1
