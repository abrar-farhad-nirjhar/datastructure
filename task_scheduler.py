import heapq

"""
Task scheduler:
"""

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, func):
        heapq.heappush(self.tasks, (priority, func))

    def execute_tasks(self):
        while self.tasks:
            yield heapq.heappop(self.tasks)



def task3():
    print("task 3")

def task7():
    print("task 7")

def task4():
    print("task 4")

def task10():
    print("task 10")

def task20():
    print("task 20")

def task15():
    print("task 15") 


ts = TaskScheduler()
ts.add_task(15, task15)
ts.add_task(20, task20)
ts.add_task(10, task10)
ts.add_task(3, task3)
ts.add_task(7, task7)
ts.add_task(4, task4)

for i in ts.execute_tasks():
    i[1]()