from task import Task


class FileCreator:
    def __init__(self):
        pass

    def write_file(self, tasks, file):

        file = open(file, 'w')
        for task in tasks:
            file.write("{}, {}, {} \n".format(task.get_offset(), task.get_computation_time(), task.get_period()))
        file.close()



