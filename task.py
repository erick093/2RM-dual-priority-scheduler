
class Task:
    def __init__(self, offset, computation_time, period, task_id=0, priority_1=0, priority_2=0, s=0):
        self.offset = offset
        self.computation_time = computation_time
        self.period = period
        self.task_id = task_id
        self.priority_1 = priority_1
        self.priority_2 = priority_2
        self.s = s

    def get_period(self):
        return self.period

    def get_computation_time(self):
        return self.computation_time

    def get_offset(self):
        return self.offset

    def get_id(self):
        return self.task_id

    def get_priority_1(self):
        return self.priority_1

    def get_priority_2(self):
        return self.priority_2

    def get_s(self):
        return self.s

    def set_priority_1(self, p):
        self.priority_1 += p
        return self.priority_1

    def set_priority_2(self, p):
        self.priority_2 += p
        return self.priority_2

    def set_s(self, s):
        self.s = s
        return self.s

    def __repr__(self):
        return "T" + str(self.task_id) + "(O:" + str(self.offset) + ", C:" + str(
            self.computation_time) + ", T:" + str(self.period) + ", P1:" + str(self.priority_1) + ", P2:" + str(
            self.priority_2) + ", S:" + str(self.s) + ")"
