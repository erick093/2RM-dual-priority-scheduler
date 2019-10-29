from jobs import Job
from lcm import lcm


class TaskSimulator:

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
        # print("ordered tasks", self.tasks)
        # print([item.period for item in self.tasks])

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
                    priority = task.period
                    wcet = task.computation_time
                    task_id = task.id
                    cj[task.id] += 1
                    #print(cj)
                    jobs.append(Job(start, end, wcet, priority, task_id, job_id=cj[task.id]))

        #print(jobs)
        return jobs

    def simulateDual(self):
        self.order_tasks()
        jobs = self.create_jobs()
        hyperperiod= self.get_hyperperiod()
        print("Schedule from: 0 to: {} ; {} tasks".format(hyperperiod, len(self.tasks)))
        for time in range(0, hyperperiod):
            queue_jobs = []
            #creates jobs queue
            for job in jobs:
                if job.start <= time:
                    queue_jobs.append(job)
            queue_jobs.sort(key=lambda x: x.priority)
            #print(queue_jobs)
            if len(queue_jobs) > 0:
                print("{}-{}: T{}J{}".format(time, time + 1, queue_jobs[0].task_id, queue_jobs[0].get_job_id()))
                if time + 1 == queue_jobs[0].end and queue_jobs[0].job_usage() is False:
                    print("Missed deadline --- Stopping...")
                    return False
                    break
                if queue_jobs[0].job_usage():
                    print("T{}J{} Finished".format(queue_jobs[0].task_id, queue_jobs[0].job_id))
                    # print("lenght of jobs: ",len(jobs))
                    # print("lenght of queue: ",len(queue_jobs))
                    jobs.remove(queue_jobs[0])

            else:
                print("{}-{}: idle slot".format(time, time + 1))

        print("END")
        return True


