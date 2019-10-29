import random
from task import Task
MIN_PERIOD = 10
MAX_PERIOD = 20
MIN_OFFSET = 0
MAX_OFFSET = 5


class TaskGenerator:

    def __init__(self, total_tasks, total_utilization):
        self.total_utilization_factor = total_utilization
        self.total_tasks = total_tasks

    def distribute_utilization_factor(self):
        rand_index = []
        utilization_factors = []
        sum = 0
        for i in range(self.total_tasks):
            rand_index.append(random.randint(1, self.total_utilization_factor))
            sum += rand_index[i]

        for i in range(len(rand_index)):
            utilization_factors.append((rand_index[i] / sum) * self.total_utilization_factor)

        return utilization_factors

    def generate_tasks(self):
        tasks = []
        utilization_factors = self.distribute_utilization_factor()
        for i in range(len(utilization_factors)):
            offset = random.randrange(MIN_OFFSET, MAX_OFFSET)
            period = random.randrange(MIN_PERIOD, MAX_PERIOD)
            computation_time = int(round((utilization_factors[i]/100)*period))
            task = Task(offset, computation_time, period)
            tasks.append(task)
        return tasks



