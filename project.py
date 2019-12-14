import sys
from task_generator import TaskGenerator
from file_creator import TaskFileManager
from simulate_dual import SimulateDual
from fdms import Fdms


class Main:
    def __init__(self):
        print("Project 1 RTOS: Dual Priority")

    @staticmethod
    def generate(total_tasks, total_utilization, file):
        task_generator = TaskGenerator(total_tasks, total_utilization)
        tasks = task_generator.generate_tasks()
        TaskFileManager.write_file(tasks, file)

    @staticmethod
    def fdms(file):
        tasks = TaskFileManager.read_file(file)
        tasks_fdms = Fdms(tasks, show_data=True)
        tasks_fdms.fdms()

    @staticmethod
    def simulate(file, stop_time):
        tasks = TaskFileManager.read_file(file)
        fdms = Fdms(tasks, show_data=False)
        fdms.fdms()
        scheduler = SimulateDual(tasks, stop_time, graphing=False, show_data=True)
        result, t_id = scheduler.simulate()

    @staticmethod
    def simulate_graph(file,stop_time):
        tasks = TaskFileManager.read_file(file)
        fdms = Fdms(tasks, show_data=False)
        fdms.fdms()
        scheduler = SimulateDual(tasks, stop_time, graphing=True, show_data=False)
        scheduler.simulate()

    @staticmethod
    def execute():
        if len(sys.argv) > 1:
            mode = sys.argv[1]
            if mode == 'gen':
                if len(sys.argv) > 4:
                    Main.generate(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
                else:
                    print("Arguments missing: Please use the form: gen  number_of_tasks  utilization_percentage  "
                          "filename.txt")
            elif mode == 'fdms':
                Main.fdms(sys.argv[2])
            elif mode == 'simulation':
                Main.simulate(sys.argv[2], int(sys.argv[3]))
            elif mode == 'simulation_graph':
                Main.simulate_graph(sys.argv[2], int(sys.argv[3]))
            else:
                print("Unrecognized mode.")
        else:
            print("Insufficient arguments, please use correct syntax")


if __name__ == '__main__':
    Main.execute()


