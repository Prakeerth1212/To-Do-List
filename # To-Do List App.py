# To-Do List App

# Initialize the list to store tasks
tasks = []

def display_tasks():
    """Display the current list of tasks"""
    if tasks:
        print("\nCurrent To-Do List: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} {'(Done)' if task['done'] else ''}")
    else:
        print("\nNo tasks in the list.")

def add_task():
    """Add a task to the to-do list"""
    task_name = input("Enter the task to add: ")
    task = {'task': task_name, 'done': False}
    tasks.append(task)
    print(f"Task '{task_name}' added to the list.")

def remove_task():
    """Remove a task from the to-do list"""
    display_tasks()
    if tasks:
        try:
            task_index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['task']}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_done():
    """Mark a task as done"""
    display_tasks()
    if tasks:
        try:
            task_index = int(input("\nEnter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]['done'] = True
                print(f"Task '{tasks[task_index]['task']}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the app"""
    while True:
        print("\n=== To-Do List App ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_done()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the To-Do List app
main()
