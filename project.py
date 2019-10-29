import sys
from task_generator import TaskGenerator
from file_creator import FileCreator
from task_simulator import TaskSimulator

class Main:
    def __init__(self):
        print("Project 1 RTOS: dual priority")

    def execute(self):
        if len(sys.argv) > 1:
            argument = sys.argv[1]
            if argument == 'gen':
                if len(sys.argv) > 4:
                    task_generator = TaskGenerator(int(sys.argv[2]), int(sys.argv[3]))  # arv[2] = # of tasks ; argv[3]= Utilization

                    tasks = task_generator.generate_tasks()
                    file = FileCreator()
                    file.write_file(tasks, sys.argv[4])
                    print("Tasks written successfully ")
                else:
                    print("Arguments missing: Please use the form: gen  number_of_tasks  utilization_percentage  "
                          "filename.txt")
            elif argument == 'fdms':
                file = FileCreator()
                tasks = file.open_file(sys.argv[2])
                #print(tasks)
                task_simulator = TaskSimulator(tasks)
               # task_simulator.load_tasks()
                #task_simulator.get_hyperperiod()
                task_simulator.simulateDual()
        else:
            print("Insufficient arguments, please use correct syntax")


if __name__ == '__main__':
    main = Main()
    main.execute()


