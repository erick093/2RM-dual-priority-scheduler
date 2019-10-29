
class Task:
    def __init__(self, offset, computation_time, period, id=0):
        self.offset = offset
        self.computation_time = computation_time
        self.period = period
        self.id = id

    def get_period(self):
        return self.period

    def get_computation_time(self):
        return self.computation_time

    def get_offset(self):
        return self.offset

    def get_id(self):
        return self.id
