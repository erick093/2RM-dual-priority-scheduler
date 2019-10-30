class Job:

    def __init__(self, start, end, wcet, task_id, job_id, priority_1, priority_2, s):
        self.start = start
        self.end = end
        self.wcet = wcet
        self.usage = 0
        self.priority_1 = priority_1
        self.priority_2 = priority_2
        self.task_id = task_id
        self.job_id = job_id
        self.s = s

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_priority_1(self):
        return self.priority_1

    def set_priority_1(self, p):
        self.priority_1 = p
        return self.priority_1

    def get_priority_2(self):
        return self.priority_2

    def set_priority_2(self, p):
        self.priority_2 = p
        return self.priority_2

    def get_task_id(self):
        return self.task_id

    def get_job_id(self):
        return self.job_id

    def set_job_id(self, counter):
        self.job_id = counter
        #print(self.job_id)

    def get_usage(self):
        return self.usage

    def job_usage(self):
        self.usage += 1
        if self.usage >= self.wcet:
            #print("usageT: ", self.usage)
            return True
        else:
            #print("usageF: ", self.usage)
            return False

    # def __repr__(self):
    #     return "T"+str(self.task_id) + "J" + str(self.job_id) + " - start: " + str(self.start) + " end: " + str(
    #         self.end) + " wcet: " + str(self.wcet) + " priority_1: " + str(self.priority_1)

    def __repr__(self):
        return "T{}J{}(s:{} e:{} c:{} p1:{} p2:{} s:{})".format(self.task_id, self.job_id, self.start, self.end,
                                                                self.wcet, self.priority_1, self.priority_2, self.s)
