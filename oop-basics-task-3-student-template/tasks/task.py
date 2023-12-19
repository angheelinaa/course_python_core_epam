class Counter:
    def __init__(self, start: int = 0, stop: int = float('inf')) -> None:
        self.start = start
        self.stop = stop
        self.count = start

    def increment(self):
        if self.count < self.stop:
            self.count += 1
        else:
            print("Maximal value is reached.")

    def get(self):
        return self.count
