from task import Task


class TaskFileManager:
    def __init__(self):
        pass

    @staticmethod
    def write_file(tasks, file):
        file = open(file, 'w')
        for task in tasks:
            file.write("{}; {}; {} \n".format(task.get_offset(), task.get_computation_time(), task.get_period()))
        file.close()

    @staticmethod
    def read_file(file_name):
        tasks = []
        task_id = 0
        try:
            file = open(file_name, "r")
            for line in file:
                task_values = line.split(";")
                tasks.append(Task(int(task_values[0]), int(task_values[1]), int(task_values[2]), task_id))
                task_id += 1
            file.close()
            return tasks
        except:
            print("ERROR: File not found")







