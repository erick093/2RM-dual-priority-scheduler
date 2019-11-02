import sys
from task_generator import TaskGenerator
from file_creator import FileCreator
from simulate_dual import SimulateDual
from fdms import Fdms

class Main:
    def __init__(self):
        print("Project 1 RTOS: dual priority")

    def r_file(self, argument):
        file = FileCreator()
        tasks = file.open_file(argument)
        return tasks

    def w_file(self, tasks, argument):
        file = FileCreator()
        file.write_file(tasks, argument)
        print("Tasks written successfully")

    def execute(self):
        if len(sys.argv) > 1:
            argument = sys.argv[1]
            if argument == 'gen':
                if len(sys.argv) > 4:
                    task_generator = TaskGenerator(int(sys.argv[2]), int(sys.argv[3]))  # arv[2] = # of tasks ; argv[3]= Utilization
                    tasks = task_generator.generate_tasks()
                    self.w_file(tasks, sys.argv[4])
                    # file = FileCreator()
                    # file.write_file(tasks, sys.argv[4])
                    # print("Tasks written successfully ")
                else:
                    print("Arguments missing: Please use the form: gen  number_of_tasks  utilization_percentage  "
                          "filename.txt")
            elif argument == 'fdms':
                tasks = self.r_file(sys.argv[2])
                tasks_fdms = Fdms(tasks)
                tasks_fdms.fdms()
            elif argument == 'simulation':
                print("simulation")
                tasks = self.r_file(sys.argv[2])
                stop_time = int(sys.argv[3])
                scheduler = SimulateDual(tasks, stop_time)
                result, t_id = scheduler.simulate()


            #elif argument == 'simulation_graph':

        else:
            print("Insufficient arguments, please use correct syntax")


if __name__ == '__main__':
    main = Main()
    main.execute()


