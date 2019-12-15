from simulate_dual import SimulateDual
from lcm import get_hyperperiod

class Fdms:

    def __init__(self, tasks, show_data):
        self.tasks = tasks
        self.show_data = show_data

    def initiate_s(self):
        for task in self.tasks:
            task.set_s(task.period)

    def print_s(self):
        print("----S VALUES---")
        for task in self.tasks:
           print("Task {}: {}".format(task.get_id(), task.get_s()))

    def fdms(self):
        self.initiate_s()
        stop_point = get_hyperperiod(self.tasks)
        tasks_simulated = SimulateDual(self.tasks, stop_point, False, show_data=self.show_data)
        result, t_id = tasks_simulated.simulate()
        while not result:
            for task in self.tasks:
                if task.get_id() == t_id:
                    if task.get_s() == 0:
                        print("S = 0 for Task: {} UNFEASIBLE".format(t_id))
                        break
                    else:
                        task.set_s(task.get_s() - 1)
                        result, t_id = tasks_simulated.simulate()
        if result:
            print("Tasks scheduled successfully.")
        self.print_s()





