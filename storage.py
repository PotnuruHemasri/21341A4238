from collections import deque

class Storage:
    def __init__(self):
        self.window = deque(maxlen=10)
        self.previous_state = []

    def update_window(self, numbers):
        self.previous_state = list(self.window)
        for num in numbers:
            if num not in self.window:
                self.window.append(num)

    def get_previous_state(self):
        return self.previous_state

    def get_current_state(self):
        return list(self.window)

    def get_current_numbers(self):
        return list(self.window)

    def calculate_average(self):
        if not self.window:
            return 0
        return sum(self.window) / len(self.window)
