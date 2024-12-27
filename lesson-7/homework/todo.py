class Task:
    def __init__(self, task_id, title, description, deadline, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status

    def __repr__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.deadline}, {self.status}"

class Task_Manager:
    def __init__(self):
        print("Welcome to the TO-DO Application!\n",
              "1. Add a new task\n",
              "2. View all tasks\n",
              "3. Update a task\n",
              "4. Delete a task\n",
              "5. Filter tasks by status\n",
              "6. Save tasks\n",
              "7. Load tasks\n",
              "8. Exit")
        self.tasks = []

    def file_to_task(self):
        """Load tasks from the file into memory."""
        self.tasks = []
        try:
            with open("lesson-7/homework/todo.txt", "r") as file:
                for line in file:
                    task_id, title, description, deadline, status = line.split(", ")
                    task = Task(int(task_id), title, description, deadline, status.strip())
                    self.tasks.append(task)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

    def save_tasks(self):
        """Save tasks to the file."""
        with open("lesson-7/homework/todo.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.task_id}, {task.title}, {task.description}, {task.deadline}, {task.status}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

    def show_tasks(self):
        for task in self.tasks:
            print(task)

    def show_task(self, task_id):
        task = next((task for task in self.tasks if task.task_id == task_id), None)
        if task:
            print(task)
        else:
            print(f"Task with ID {task_id} not found.")

    def update_task(self, task_id, title, description, deadline, status):
        task2 = next((task for task in self.tasks if task.task_id == task_id), None)
        if task2:
            task.title = title
            task.description = description
            task.deadline = deadline
            task.status = status
            self.save_tasks()
            print(f"Task with ID {task_id} updated successfully!")
        else:
            print(f"Task with ID {task_id} not found.")
            return

    def mark_as_done(self, task_id):
        self.update_task(task_id, "Done")

    def mark_as_undone(self, task_id):
        self.update_task(task_id, "Undone")

    def show_done_tasks(self):
        for task in self.tasks:
            if task.status == "Done":
                print(task)

    def show_undone_tasks(self):
        for task in self.tasks:
            if task.status == "Undone":
                print(task)

# Main program
a = Task_Manager()
a.file_to_task()  # Load tasks from the file when the program starts

option = int(input("Enter your choice: "))

if option == 1:
    task_id = int(input("Enter task ID: "))
    title = input("Enter Title: ")
    description = input("Enter Description: ")
    deadline = input("Enter Due Date (YYYY-MM-DD): ")
    status = input("Enter Status: ")
    task = Task(task_id, title, description, deadline, status)
    a.add_task(task)
    print("Task added successfully!")
elif option == 2:
    print("Tasks:")
    a.show_tasks()
elif option == 3:
    task_id = int(input("Enter task ID: "))
    title = input("Enter Title: ")
    description = input("Enter Description: ")
    deadline = input("Enter Due Date (YYYY-MM-DD): ")
    status = input("Enter Status: ")
    a.update_task(task_id, title, description, deadline, status)
    print("Task updated successfully!")
elif option == 4:
    task_id = int(input("Enter task ID: "))
    a.remove_task(task_id)
    print("Task removed successfully!")
elif option == 5:
    status = input("Enter Status (Done/Undone): ")
    if status == "Done":
        a.show_done_tasks()
    elif status == "Undone":
        a.show_undone_tasks()
elif option == 6:
    a.save_tasks()
    print("Tasks saved successfully!")
elif option == 7:
    a.file_to_task()
    print("Tasks loaded successfully!")
elif option == 8:
    print("Exiting...")
    exit()

