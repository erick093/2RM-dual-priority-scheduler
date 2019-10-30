from jobs import Job
from lcm import lcm


class SimulateDual:

    def __init__(self, tasks):
        self.tasks = tasks

    def get_hyperperiod(self):
        hyperperiod = []
        for task in self.tasks:
            hyperperiod.append(task.period)
        hyperperiod = lcm(hyperperiod)
        #print("Hyperperiod: ", hyperperiod)
        # self.get_utilization()
        return hyperperiod

    def order_tasks(self):
        self.tasks.sort(key=lambda x: x.period)
        print("ordered tasks by period", self.tasks)
        # print([item.period for item in self.tasks])

    def assign_priority_1(self):
        #c = 1
        c = len(self.tasks) + 1
        for task in self.tasks:
            task.set_priority_1(c)
            c += 1
        print("Tasks assigned P1: {}".format(self.tasks))

    def assign_priority_2(self):
        #c = 1
        c = 1
        for task in self.tasks:
            task.set_priority_2(c)
            c += 1
        print("Tasks assigned P2: {}".format(self.tasks))

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
        #job_id = 0
        cj = self.counter()
        hyperperiod = self.get_hyperperiod()
        for time in range(0, hyperperiod):
            for task in self.tasks:
                if (time - task.offset) % task.period == 0 and time >= task.offset:
                    start = time
                    end = start + task.period
                    priority_1 = task.priority_1
                    priority_2 = task.priority_2
                    wcet = task.computation_time
                    task_id = task.task_id
                    cj[task.task_id] += 1
                    s = start + task.s
                    #print(cj)
                    jobs.append(Job(start, end, wcet, task_id, cj[task.task_id], priority_1, priority_2, s))

        #print(jobs)
        return jobs

    def simulate(self):
        self.order_tasks()
        self.assign_priority_1()
        self.assign_priority_2()
        jobs = self.create_jobs()
        hyperperiod = self.get_hyperperiod()
        print("Schedule from: 0 to: {} ; {} tasks".format(hyperperiod, len(self.tasks)))
        for time in range(0, hyperperiod):
            queue_jobs = []

            #test code
            for job in jobs:
                if time + 1 == job.s:
                    print("Found Job {} time {} equal s {}".format(job.task_id, time + 1, job.s))
                    job.set_priority_1(job.get_priority_2())
            #test code


            #creates jobs queue
            for job in jobs:
                if job.start <= time:
                    queue_jobs.append(job)
            queue_jobs.sort(key=lambda x: x.priority_1)
            #print(queue_jobs)


            if len(queue_jobs) > 0:
                print("{}-{}: T{}J{}".format(time, time + 1, queue_jobs[0].task_id, queue_jobs[0].get_job_id()))
                if time + 1 == queue_jobs[0].end and queue_jobs[0].job_usage() is False:
                    print("Missed deadline --- Stopping...")
                    return False, queue_jobs[0].get_task_id()
                    #break
                if queue_jobs[0].job_usage():
                    print("T{}J{} Finished".format(queue_jobs[0].task_id, queue_jobs[0].job_id))
                    # print("lenght of jobs: ",len(jobs))
                    # print("lenght of queue: ",len(queue_jobs))
                    jobs.remove(queue_jobs[0])

            else:
                print("{}-{}: idle slot".format(time, time + 1))

        print("END")
        return True, -1


