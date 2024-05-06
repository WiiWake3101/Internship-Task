class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        del self.tasks[task_index]

    def mark_task_completed(self, task_index):
        self.tasks[task_index]["completed"] = True

    def display_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['completed']}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                task, completed = line.strip().split(',')
                self.tasks.append({"task": task, "completed": bool(completed)})


def main():
    todo_list = ToDoList()
    todo_list.load_from_file("tasks.txt")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(
                input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            todo_list.save_to_file("tasks.txt")
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
