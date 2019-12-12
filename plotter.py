import matplotlib.pyplot as plt
import numpy as np


class Plotter:

    def __init__(self, tasks, stop_time):
        self.tasks = tasks
        self.stop_time = stop_time
        plt.xlabel("Time")
        plt.ylabel("Tasks")
        plt.grid(True, linestyle="--")

    def plot_tasks(self):
        for task in self.tasks:
            period = task.get_period()
            offset = task.get_offset()
            task_id = task.get_id()



