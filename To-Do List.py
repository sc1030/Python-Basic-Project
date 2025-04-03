# Initialize an empty list to store tasks
'''tasks = []

# Function to display the menu

def show_menu():
    print("\n1. Add Task \n2. View Tasks \n3. Exit")

# Function to add a task
def add_task():
    task = input("Enter task: ")  # Get user input for the task
    tasks.append(task)  # Append task to the list
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):  # Loop through the list with index
            print(f"{i}. {task}")  # Print task number and task name

# Main program loop
while True:
    show_menu()
    choice = input("Choose an Option: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid Option! Please try again.")
'''


# Task Manager Application

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTask Manager")
    print("=" * 20)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Function to clear all tasks
def clear_tasks():
    global tasks
    if tasks:
        confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
        if confirm == "yes":
            tasks = []
            print("All tasks cleared!")
        else:
            print("Operation canceled.")
    else:
        print("No tasks to clear!")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option! Please try again.")
