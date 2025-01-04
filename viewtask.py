def view_tasks(self):
    if not self.tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(self.tasks, start=1):
        status = "Done" if task['completed'] else "Pending"
        print(f'{index}. {task["task"]} - {status}')
