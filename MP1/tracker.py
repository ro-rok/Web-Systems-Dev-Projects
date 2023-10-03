from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # make sure any checks/conditions clearly display an appropriate message of what failed
    
    if not name or not description or not due:
        print("Task not added, because of missing data \n")
    else:
        try:
            task["name"] = name
            task["description"] = description
            task["due"] = str_to_datetime(due)
            task["lastActivity"] = datetime.now()
            tasks.append(task)
            print("Task added\n")
        except:
            print("Task not added due to an invalid due date format. Please use 'mm/dd/yy hh:mm:ss' or 'yyyy-mm-dd hh:mm:ss'.")

    save()
        
    # rk868 10/2/2023
    # First, I checked if the name, description, and due date were provided. If not, I printed a message saying the task was not added because of missing data.
    # If the name, description, and due date were provided, I tried to update the name, description, and due date in the task template.
    # If the due date was not in the correct format, I printed a message saying the task was not added due to an invalid due date format.
    # Otherwise, I updated lastActivity with the current datetime value, added the new task to the tasks list, and printed a message saying the task was added.
    # Lastly, I called save() to save the changes to the json file.


def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    if len(tasks) == 0:
        print("There are no tasks in the Task Tracker \n" ) 
    elif index <0 or index >= len(tasks):
        print(f"Invalid index, must be between 1 and {len(tasks)} \n")
    else:
        view_task(index)
        name = input(f"What's the name of this task? (TODO name) \n").strip()
        desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
        update_task(index, name=name, description=desc, due=due)

    # rk868 10/2/2023
    # First, I checked if there were any tasks in the Task Tracker and if the index was valid.
    # If not, I printed a message saying there were no tasks in the Task Tracker or the index was invalid.
    # If there were tasks in the Task Tracker and the index was valid, I called view_task(index) to show the existing value of each property.
    # Then, I prompted the user to enter the new name, description, and due date of the task.
    # Lastly, I called update_task(index, name=name, description=desc, due=due) to update the name, description, and due date of the task.


def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    if len(tasks) == 0:
        print("There are no tasks in the Task Tracker \n")
        return
    elif index <0 or index >= len(tasks):
        print(f"Invalid index, must be between 1 and {len(tasks)} \n")
        return

    task = tasks[index]

    if (not name and not description and not due) or (name == task["name"] and description == task["description"] and due == task["due"]) :
        print("Task not updated due to missing data or no changes \n")
        return
    
    if name:
        task["name"] = name
    if description:
        task["description"] = description
    if due:
        try:
            task["due"] = str_to_datetime(due)
        except:
            print("Task not updated due to an invalid due date format. Please use 'mm/dd/yy hh:mm:ss' or 'yyyy-mm-dd hh:mm:ss'.")
            return
    task["lastActivity"] = datetime.now()
    print("Task updated. \n")

    save()

    # rk868 10/3/2023
    # First, I checked if there were any tasks in the Task Tracker and if the index was valid.
    # If not, I printed a message saying there were no tasks in the Task Tracker or the index was invalid.
    # If there were tasks in the Task Tracker and the index was valid, I checked if the name, description, and due date were provided.
    # Or if the name, description, and due date were the same as the original task property value.
    # If the name, description, and due date were not provided or the name, description, and due date were the same as the original task property value,
    # I printed a message saying the task was not updated.
    # Else, I tried to update the name, description, and due date in the task template.
    # If the due date was not in the correct format, I printed a message saying the task was not updated due to an invalid due date format.
    # Otherwise, I updated lastActivity with the current datetime value and printed a message saying the task was updated.
    # Lastly, I called save() to save the changes to the json file.

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    if len(tasks) == 0:
        print("There are no tasks in the Task Tracker \n" )
        return
    elif index <0 or index >= len(tasks):
        print(f"Invalid index, must be between 1 and {len(tasks)} \n")
        return
    
    task = tasks[index]
    
    if not task["done"]:
        task["done"] = datetime.now()
        print("Task completed \n")
    else:
        print("Task already completed \n")

    save()

    # rk868 10/3/2023
    # First, I checked if there were any tasks in the Task Tracker and if the index was valid.
    # If not, I printed a message saying there were no tasks in the Task Tracker or the index was invalid.
    # If there were tasks in the Task Tracker and the index was valid, I checked if the task was already completed.
    # If the task was not already completed, I recorded the current datetime as the value.
    # Then, I printed a message saying the task was completed. Otherwise, I printed a message saying the task was already completed.
    # Lastly, I called save() to save the changes to the json file.

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {} # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes

    if len(tasks) == 0:
        print("There are no tasks in the Task Tracker \n" )
        return
    elif index <0 or index >= len(tasks):
        print(f"Invalid index, must be between 1 and {len(tasks)} \n")
        return
    
    task = tasks[index]

    print(f"""
        [{'x' if task['done'] else ' '}] Task{index+1}: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))

    # rk868 10/2/2023
    # First, I checked if there were any tasks in the Task Tracker and if the index was valid.
    # If not, I printed a message saying there were no tasks in the Task Tracker or the index was invalid.
    # If there were tasks in the Task Tracker and the index was valid, 
    # I printed the task's name, index, description, lastActivity, due date, and completed status.


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}# <-- this is a placeholder to populate based on the above requirements
    # do your print logic here

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()