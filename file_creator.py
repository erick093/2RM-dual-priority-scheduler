from task import Task


class FileCreator:
    def __init__(self):
        pass

    def write_file(self, tasks, file):

        file = open(file, 'w')
        for task in tasks:
            file.write("{}; {}; {} \n".format(task.get_offset(), task.get_computation_time(), task.get_period())) #generates tuple(Offset;WCET,Period)
        file.close()

    def open_file(self,file):
        tasks = []
        task_id = 0
        f = open(file, "r")
        for x in f:
            line = x.split(";")
            tasks.append(Task(int(line[0]), int(line[1]), int(line[2]), task_id))
            task_id += 1
        f.close()
        return tasks





