from simulate_dual import SimulateDual
from lcm import get_hyperperiod

class Fdms:

    def __init__(self, tasks):
        self.tasks = tasks

    def initiate_s(self):
        for task in self.tasks:
            task.set_s(task.period)

    def print_s(self):
        for task in self.tasks:
            print("Task {}: {}".format(task.get_id(), task.get_s()))

    def fdms(self):
        self.initiate_s()
        #print("Tasks initialized with S: ", self.tasks)
        #print(self.tasks)
        stop_point = get_hyperperiod(self.tasks)
        #print("HP: {}".format(stop_point))
        tasks_simulated = SimulateDual(self.tasks, stop_point, False, False)
        result, t_id = tasks_simulated.simulate()


        # while not result:
        #     if self.tasks[t_id].get_s() == 0:
        #         print("S = 0 for Task: {} UNFEASIBLE".format(t_id))
        #         break
        #     else:
        #         #print("Task {} missed deadline with S: {}.".format(t_id, self.tasks[t_id].get_s()))
        #         for task in self.tasks:
        #             if task.get_id() == t_id:
        #                 #print("Task {} missed deadline with S: {}.".format(t_id, task.get_s()))
        #                 task.set_s(task.get_s() - 1)
        #                 result, t_id = tasks_simulated.simulate()
        #         #self.tasks[t_id].set_s(self.tasks[t_id].get_s() - 1)
        #         #result, t_id = tasks_simulated.simulate()

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
        #self.print_s()





