tasks = []

def show_menu ():

    print("\n ----TO DO LIST----")
    print(" Add a Task ")

    print(" View Task")

    print(" Mark Test as done ")

    print(" Delete a Task ")

    print(" Exit ")

def add_task ():

    task = input (" Enter task :  ")
    tasks.append({"task":task , "done": False})
    print(f"task '{task}' added!")


def view_task():
    if not tasks:
        print("no tasks yet!")
    else :

        print("\n Your Tasks : ")

        for index , task in enumerate(tasks , start = 1):

            status = "done" if task["done"] else "Not done"

            print(f"{index}. {task['task']} [{status}]")

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done"))-1
        if 0<= index < len(tasks):
            tasks[index]["Done"] = True

            print("Marked as done! ")
        else:
            print("invalid number!")

    except ValueError:
        print("enter a valid number of task!")

def del_task():
    view_task()

    if not tasks:
        return

    try:
        index = int("enter number of the task you want to delete!")

        if 0<= index < len(tasks):
            tasks.pop(index)

            print("sucessfully deleted!")

        else:

            print("invlaid number! ")

    except ValueError:
        ("pl enter valid number.")

    
show_menu()

add_task()

view_task()

mark_done()

del_task()




