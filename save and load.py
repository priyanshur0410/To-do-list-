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
