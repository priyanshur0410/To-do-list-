import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task['completed'] else "Pending"
            print(f'{index}. {task["task"]} - {status}')

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task {task_number} marked as completed.')
        else:
            print("Invalid task number.")

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
        print("Tasks saved to file.")

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No saved tasks found.")

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            todo_list.save_to_file()
        elif choice == "5":
            todo_list.load_from_file()
        elif choice == "6":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")
