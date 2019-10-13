
class Task:
    def __init__(self, offset, computation_time, period):
        self.offset = offset
        self.computation_time = computation_time
        self.period = period

    def get_period(self):
        return self.period

    def get_computation_time(self):
        return self.computation_time

    def get_offset(self):
        return self.offset
