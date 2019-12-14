from jobs import Job

import matplotlib.pyplot as plt
import numpy as np

class SimulateDual:

    def __init__(self, tasks, stop_point, graphing=False, show_data=False):
        self.tasks = tasks
        self.stop_point = stop_point
        self.graphing = graphing
        self.show_data = show_data

    def plot_tasks(self, tasks_order, fx, tx, task_deadline, task_s, task_init):

        plt.hlines(tasks_order, fx, tx, linewidth=20, colors='green')
        plt.plot(task_deadline, tasks_order, 'ro', marker='v', label="Deadline")
        plt.plot(task_s, tasks_order, 'bo', marker='|', label="S", markersize=10.0)
        plt.plot(task_init, tasks_order, 'ko', marker='.', label="Start", markersize=4.0)
        plt.legend(loc='center right', prop={'size': 8})
        plt.title('Dual Priority RM + RM Scheduler')
        plt.grid(True)
        plt.xlabel("Time")
        plt.xticks(np.arange(min(fx), max(tx) + 1, 5.0))
        plt.savefig("scheduler_{}_tasks.png".format(len(self.tasks)))

    def order_tasks(self):
        self.tasks.sort(key=lambda x: x.period)
        # print("ordered tasks by period", self.tasks)

    def assign_priority_1(self):
        c = len(self.tasks) + 1
        for task in self.tasks:
            task.set_priority_1(c)
            c += 1
        #print("Tasks assigned P1: {}".format(self.tasks))

    def assign_priority_2(self):
        c = 1
        for task in self.tasks:
            task.set_priority_2(c)
            c += 1
        #print("Tasks assigned P2: {}".format(self.tasks))

    def get_utilization(self):
        u = 0
        for task in self.tasks:
            u += task.computation_time / task.period
        print("Utilization: ", u)
        return u

    def counter(self):
        count = []
        for task in self.tasks:
            count.append(0)
        #print(count)
        return count

    def create_jobs(self):
        jobs = []  # jobs
        cj = self.counter()
        #hyperperiod = get_hyperperiod(self.tasks)
        for time in range(0, self.stop_point):
            for task in self.tasks:
                if (time - task.offset) % task.period == 0 and time >= task.offset:
                    start = time
                    end = start + task.period
                    priority_1 = task.priority_1
                    priority_2 = task.priority_2
                    wcet = task.computation_time
                    task_id = task.task_id
                    s = start + task.s
                    jobs.append(Job(start, end, wcet, task_id, cj[task.task_id], priority_1, priority_2, s))
                    cj[task.task_id] += 1

        #print(jobs)
        return jobs

    def print_intervals(self, task_id, job_id, start_time, end_time, is_idle):
        if self.show_data:
            if is_idle == 1:
                message = "{}-{}: Idle slot".format(start_time, end_time)
            else:
                message = "{}-{}: T{}J{}".format(start_time, end_time, task_id, job_id)
            print(message)


    def simulate(self):
        #arrays used for plotting
        tasks_order = []
        task_deadline = []
        task_s = []
        task_init = []

        fx = []
        tx = []
        self.order_tasks()
        self.assign_priority_1()
        self.assign_priority_2()
        jobs = self.create_jobs()
        #hyperperiod = get_hyperperiod(self.tasks)
        #print("Schedule from: 0 to: {} ; {} tasks".format(self.stop_point, len(self.tasks)))
        last_task_id = -1
        last_job_id = -1
        start_job_time = 0
        for time in range(0, self.stop_point):
            queue_jobs = []
            for job in jobs:
                if time == job.s:
                    #print("T:{}J:{} time:{} s:{} P1:{}--->P2:{}".format(job.task_id, job.job_id, time, job.s,
                     #                                                   job.priority_1, job.priority_2))
                    job.set_priority_1(job.get_priority_2())
                if job.start <= time:
                    queue_jobs.append(job)
            queue_jobs.sort(key=lambda x: x.priority_1)
            #print("Printing queue", queue_jobs)

            if len(queue_jobs) > 0:
                tasks_order.append("Task{}".format(queue_jobs[0].task_id))
                #task_test_deadline.append(("Task{}".format(queue_jobs[0].task_id), queue_jobs[0].end))
                task_deadline.append(queue_jobs[0].end)
                task_s.append(queue_jobs[0].s)
                task_init.append(queue_jobs[0].start)
                fx.append(time)
                tx.append(time+1)
                if(last_task_id != -1 and last_job_id != -1 and (last_job_id != queue_jobs[0].get_job_id()
                        or last_task_id != queue_jobs[0].task_id)):
                    self.print_intervals(last_task_id,last_job_id, start_job_time, time, 0)
                    start_job_time = time
                last_task_id = queue_jobs[0].task_id
                last_job_id = queue_jobs[0].get_job_id()
                #print("{}-{}: T{}J{}".format(time, time + 1, queue_jobs[0].task_id, queue_jobs[0].get_job_id()))
                job_usage = queue_jobs[0].job_usage()
                if job_usage:
                    #print("T{}J{} Finished".format(queue_jobs[0].task_id, queue_jobs[0].job_id))
                    jobs.remove(queue_jobs[0])
                else:
                    for job in jobs:
                        if time + 1 == job.end:
                            if self.show_data:
                                print("Missed deadline --- Stopping...")
                            self.print_intervals(last_task_id, last_job_id, start_job_time, time + 1, 0)
                            return False, job.get_task_id()
            else:
                if ( last_task_id != -1) :
                    self.print_intervals(last_task_id, last_job_id, start_job_time, time, 0)
                last_task_id = -1
                last_job_id = -1
                start_job_time = time
                self.print_intervals(0, 0, time, time + 1, 1)
        if (last_task_id != -1):
            self.print_intervals(last_task_id, last_job_id, start_job_time, time+1, 0)
        if self.show_data:
            print("END")
        if self.graphing:
            self.plot_tasks(tasks_order, fx, tx, task_deadline, task_s, task_init)
        return True, -1


