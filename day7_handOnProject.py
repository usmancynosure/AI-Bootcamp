import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    
    # If file does not exist, create an empty file
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass  # Creates an empty file

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:  # Ensure line is not empty
                task_id, title, status = line.split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    task_id = max(tasks.keys(), default=0) + 1  # Assign a new unique task ID
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added successfully.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for task_id, task in tasks.items():
            print(f"{task_id}: {task['title']} - {task['status']}")
        print("-----------------")

# Mark task as complete
def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID to mark as completed: ").strip())
        if task_id in tasks:
            tasks[task_id]["status"] = "complete"
            print(f"Task {task_id} marked as completed.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Task ID.")

# Delete a task
def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        if task_id in tasks:
            deleted_task = tasks.pop(task_id)
            print(f"Task {task_id} ('{deleted_task['title']}') deleted successfully.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Task ID.")

# Main function to run the task manager
def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
