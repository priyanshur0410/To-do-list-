def mark_completed(self, task_number):
    if 0 < task_number <= len(self.tasks):
        self.tasks[task_number - 1]["completed"] = True
        print(f'Task {task_number} marked as completed.')
    else:
        print("Invalid task number.")
