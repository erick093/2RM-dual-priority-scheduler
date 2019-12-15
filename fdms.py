from simulate_dual import SimulateDual
from lcm import get_hyperperiod

import numpy as np


class Fdms:

    def __init__(self, tasks, show_data):
        self.tasks = tasks
        self.show_data = show_data

    def initiate_s(self):
        for task in self.tasks:
            task.set_s(task.period)

    def print_s(self):
        if self.show_data:
            print("----S VALUES---")
            for task in self.tasks:
               print("Task {}: {}".format(task.get_id(), task.get_s()))

    def fdms(self):
        self.initiate_s()
        stop_point = get_hyperperiod(self.tasks)
        tasks_simulated = SimulateDual(self.tasks, stop_point, False, show_data=self.show_data)
        result, t_id = tasks_simulated.simulate()
        is_not_feasible = False
        while not is_not_feasible and not result:
            for task in self.tasks:
                if task.get_id() == t_id:
                    if task.get_s() == 0:
                        print("S = 0 for Task: {} UNFEASIBLE".format(t_id))
                        is_not_feasible = True
                        break
                    else:
                        task.set_s(task.get_s() - 1)
                        result, t_id = tasks_simulated.simulate()
        if result:
            print("Tasks scheduled successfully.")
        self.print_s()





