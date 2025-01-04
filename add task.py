def add_task(self, task):
    self.tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')
