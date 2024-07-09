# To-Do List Application

# Function to display menu options
def display_menu():
    print("======= TO-DO LIST APPLICATION =======")
    print("1. View To-Do List")
    print("2. Add Your Task")
    print("3. Mark The Task as Completed")
    print("4. Delete Task")
    print("5. Save and Quit")
    print("***************************")

# Function to view current To-Do list
def view_todo_list(todo_list):
    if not todo_list:
        print("Your To-Do list is empty. Add The List If You're Ready.")
    else:
        print("======= TO-DO LIST =======")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the To-Do list
def add_task(todo_list):
    task = input("Enter Your task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the To-Do list.")

# Function to mark a task as completed
def mark_task_completed(todo_list):
    view_todo_list(todo_list)
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(todo_list):
            print(f"Task '{todo_list[task_index]}' marked as completed.")
            todo_list.pop(task_index)
        else:
            print("Your Task Number is Invalid. Please try again.")
    except ValueError:
        print("Input Not Found. Please enter a valid task number.")

# Function to delete a task from the To-Do list
def delete_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(todo_list):
            print(f"Task '{todo_list[task_index]}' deleted.")
            todo_list.pop(task_index)
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Your Input Is Invalid. Please enter a valid task number.")

# Main function to run the To-Do list application
def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Saving your To-Do list.Complete With The Dedication With What You started. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
