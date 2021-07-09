# Create a todo list app.

tasks = []

# Add Task:
# Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low.
def add_task(choice, tasks):
    name = input("\nEnter the name of your task: ")
    priority = input("\nEnter priority of task: ")

    task = {"Task": name, "Priority": priority}

    tasks.append(task)

    return tasks

# Delete Task:
# Show user all the tasks along with the index number of each task. User can then enter the index number of the task to delete the task.
def delete_task(choice, tasks):
    for index in range(len(tasks)):
        print(f"{index + 1} - {tasks[index]['Task']} - {tasks[index]['Priority']}")
    num = int(input("\nEnter the number of the task you would like to delete: "))
    for index in range(len(tasks)):
        if tasks[index] == tasks[num - 1]:
            print(f"\nThe task {tasks[num -1]['Task']} has been deleted from your To-Do list.")
            del tasks[index]
            break
    return tasks

# View all tasks:
# Allow the user to view all the tasks in the following format:
def view_tasks(choice, tasks):
    if len(tasks) == 0:
        print("\nYou have no tasks.")
    for index in range(len(tasks)):
        print(f"{index + 1} - {tasks[index]['Task']} - {tasks[index]['Priority']}")

# When the app starts it should present user with the following menu:
# Press 1 to add task
# Press 2 to delete task
# Press 3 to view all tasks
# Press q to quit
# The user should only be allowed to quit when they press 'q'.

while True:
    choice = input(
        "\nPress 1 to add task \nPress 2 to delete task \nPress 3 to view all tasks \nPress q to quit \n"
    )
    if choice == "q":
        print("\nGoodbye\n")
        break
    elif choice == "1":
        add_task(choice, tasks)

    elif choice == "2":   
        delete_task(choice, tasks)
    
    elif choice == "3":
        view_tasks(choice, tasks)
    
    else:
        print("\nInvalid option\n")
        
