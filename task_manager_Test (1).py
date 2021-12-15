# import date will assist in printing out the current date into the task file;https://stackoverflow.com/questions/35010492/import-txt-with-date-and-time
from datetime import datetime
from datetime import date
from os import remove
import re

# The function of this set of code is to register a user
# line 15 through  checks to see if the user at the time is the admin and if not they will not be allowed to use this option
# lines 18 through 23 checks if the username is already in the user.txt file and will request for a new name if the name entered already exists
# Line 24 through 30 helps to assign a password to the username entered in the previous lines and check if the password is the same by asking for confirmation
# the


def reg_user():
    if username == "admin":
        file = open("user.txt", "r+")
        file_dup = file.readlines()
        name = input("please enter a username: ")
        for line in file_dup:
            valid_user, valid_password = line.split(",")
            if name == valid_user:
                print("this username is already in use. Please create a new name.")
                reg_user()
        if name != valid_user:
            password_in = input("please enter a Password: ")
            password_con = input("Please confirm your password: ")
            if password_in == password_con:
                combine_entry = f"{name},{password_con}\n"
                file.write(combine_entry)
                file.close()
            else:
                print("password doesn't match.")
                reg_user()
        file.close()
    else:
        print("Only the user under the name 'admin' can register a new user")
        print(
            "You are not able to register a new user as you are not the user 'admin'."
        )
        return


# this add task funtion helps to assign tasks to users and then saves them into the task file
def add_task():
    file2 = open("tasks.txt", "a")
    username1 = input("Please enter the username: ")
    task_name1 = input("Please enter the name of the task you like to assign :")
    task_type1 = input("PLease enter the description of task you are assigning :")
    due_date = input("What is the due date? ")
    date_assigned = date.today()
    completed = "No"
    file2.writelines(
        username1
        + ","
        + task_name1
        + ","
        + task_type1
        + ","
        + due_date
        + ","
        + str(date_assigned)
        + ","
        + completed
        + "\n"
    )
    file2.close()
    print("=" * 50)
    print("=" * 50)
    print("=" * 50)


# the for loop is split up making it easier for the program to run and display the needed in the correct order
def view_all():
    file3 = open("tasks.txt", "r")
    data0 = file3.readlines()
    for line in data0:
        (
            person,
            task_name,
            description,
            completion_date,
            date_assigned,
            task_com,
        ) = line.strip().split(",")
        print("task assigned to : ", person)
        print("task name: ", task_name)
        print("task description: ", description)
        print("due date: ", completion_date)
        print("date assigned: ", date_assigned)
        print("has the assignment been completed: ", task_com)
        print("=" * 40)
        print("=" * 40)
    file3.close()


# the enumerate function helps to assign a numeric value to the tasks and "i" is used to represent the numbers
# the edit_task input allows for the user to select the numbered task that they want to edit


def view_mine():

    tasks_file = open("tasks.txt", "r+")

    data = tasks_file.readlines()

    task_counter = 0
    task_number = []
    for i, line in enumerate(data):
        (
            person,
            task_name,
            description,
            completion_date,
            date_assigned,
            task_com,
        ) = line.split(",")

        if username in person:
            task_counter += 1
            print(f"TASK NUMBER: ", i)
            print(f"task assigned to: ", person)
            print(f"task name: ", task_name)
            print(f"task description: ", description)
            print(f"due date: ", completion_date)
            print(f"date assigned: ", date_assigned)
            print(f"has the assignment been completed: ", task_com)
            print("-" * 40)
            task_number.append(i)

    if (task_counter == 0):
            
        print("")
        print("You have no tasks at this current moment.")
        print("Well done!")
        print("")
    #If the counter is 0 then it displays the corresponding messages to the user.


    if (task_counter != 0):   
        edit_task = int(
            input(
                "Would like to edit a task?\n"
                "If you would, please enter the task number and if you"
                "would like to return to the main menu, please enter '-1': "
            )
        )
            
    # the -1 answer will send the user back to the main menu
    if edit_task == -1:
        print("=" * 50)
        print("=" * 50)
        print("=" * 50)

    # Winton and Whihan.pre helped me to fully understand how to use enumerate
    # the function here is to help the user edit the name, date or completion of the task
    # the function of the truncate(0) helps to clear out the task file and rewrite the content back into the file with the edited content
    new_data = []
    if edit_task in task_number:
        tasks_file.truncate(0)
        for i, line in enumerate(data):
            (
                assigned_to,
                task_name,
                description,
                start_date,
                completion_date,
                status,
            ) = line.strip(" ").split(",")
            line = line.strip().split(",")
            if edit_task != i:
                tasks_file.write(
                    f"{assigned_to},{task_name},{description},{start_date},{completion_date},{status}"
                )
            if edit_task == i:
                change_opt = input(
                    "would you like to edit:\n"
                    "who the task was assigned to - 'name'\n"
                    "the due date of the task - 'date'\n"
                    "or the completion of the task - 'completion'"
                )
                if change_opt == "name":
                    new_name = input("Please enter the new name:")
                    line[0] = new_name
                    line = ",".join(line)
                    new_data.append(line)
                    tasks_file.write(str(line).lstrip() + "\n")

                if change_opt == "date":
                    new_date = input("Please enter the new due date: ")
                    line[3] = new_date
                    line = ",".join(line)
                    new_data.append(line)
                    tasks_file.write(str(line) + "\n")

                if change_opt == "completion":
                    complete = input("Has the task been completed, 'Yes' or 'No': ")
                    line[-1] = complete
                    line = ",".join(line)
                    new_data.append(line)
                    tasks_file.write(str(line) + "\n")
    tasks_file.close()


def gen_report():
    # This will open the task_overview file so we can write data to it from the other files and program.
    with open("task_overview.txt", "r+") as task_overview:

        Task_name = ""
        Assigned_to = ""
        description = ""
        assigned_date = ""
        date_due = ""
        completed = ""
        # These variables above will be used to help gather and use the info from the tasks.txt file.

        with open("tasks.txt", "r+") as tasks:
            # This opens the tasks.txt file so we can get the information we need about the tasks to generate reports.

            tasks.seek(0)

            num_tasks = 0
            num_completed = 0
            num_uncompleted = 0
            num_overdue = 0
            num_overdue_uncompleted = 0
            # The above variables will store all the relevant data we will be writing to the file of task_overview.txt.

            for line in tasks:
                num_tasks += line.count(line)
                splitline = line.replace("\n", "")
                splitline = line.strip()
                splitline = line.split(",")
                Task_name = str(splitline[1:2])
                Assigned_to = str(splitline[0:1])
                description = str(splitline[2:3])
                assigned_date = str(splitline[3:4])
                date_due = str(splitline[4:5])
                completed = str(splitline[5:6])

                overdue_date_list = ""
                overdue_date_list = str(date_due).strip()
                overdue_date_list = overdue_date_list[2:12]
                # The above is the date_due split and then put into a list and then into different variables for use below.

                overdue_date = datetime.strptime(overdue_date_list, '%Y-%m-%d')
                current_date = datetime.today()

                if "Yes" in completed:
                    num_completed += 1
                # If the variable contains the word 'Yes' then it will add 1 to the num_completed variable for completed tasks.
                if "No" in completed:
                    num_uncompleted += 1
                # If the variable contains the word 'No' then it will add 1 to the num_uncompleted variable for the uncompleted tasks.
                if (current_date > overdue_date) and ("No" in completed):
                    num_overdue += 1
                # If the current date of the user is greater, meaning it's past the due date then it will add 1 to the num_overdue variable for overdue tasks.
                if ("No" in completed) and (current_date > overdue_date):
                    num_overdue_uncompleted += 1
                # The above takes the uncompleted and overdue tasks and places them under one variable for both uncompleted and overdue tasks.

            precentage_uncompleted = (num_uncompleted / num_tasks) * 100
            percentage_overdue = (num_overdue / num_tasks) * 100
            # These two variables will occur after the whole loop is done to ensure we get an accurate percentage of each.

        task_overview.write(f"The number of tasks are: {num_tasks}.\n")
        task_overview.write(f"The number of completed tasks are: {num_completed}.\n")
        task_overview.write(f"The number of uncompleted tasks are: {num_uncompleted}.\n")
        task_overview.write(f"The number of overdue tasks are: {num_overdue}.\n")
        task_overview.write(f"The number of uncompleted and overdue tasks are: {num_overdue_uncompleted}.\n")
        task_overview.write(f"The percentage of uncompleted tasks are: {precentage_uncompleted}.\n")
        task_overview.write(f"The percentage of overdue tasks are: {percentage_overdue}.\n")
        # The above writes all the necessary data to the task_overview.txt file.

    tasks.close()
    task_overview.close()
    # This closes the files to prevent bugs and unnecessary memory usage.

    # this will open the user_overview.txt file so that we can write data to it from other files during the run of the program.
    with open("user_overview.txt", "r+") as user_overview:

        amount_users = 0
        # This variable will store the amount of users.

        # This will open the user.txt file for use.
        with open("user.txt", "r+") as users:

            users.seek(0)

            user_content = users.read()
            user_colist = user_content.split("\n")
            # The above will read and make a list of the content within the file of users.txt

            for i in user_colist:
                if i:
                    amount_users += 1
            # This loop will run through the list of the user_colist and add 1 to the counter per index/line in the list.

        user_overview.write(f"The total amount of users is {amount_users}\n")
        # The above will count the amount of users in the file and write it to the new file.

        # This will open the tasks.txt file for use.
        with open("tasks.txt", "r+") as tasks:

            tasks.seek(0)
            tasks_info = tasks.readlines()
            amount_tasks = 0
            num_users = 0
            users = ""

            for line in tasks_info:
                num_users += 1
                amount_tasks += 1
                temp = line.split(",")
                users += temp[0] + " "

                overdue_date_list = ""
                overdue_date_list = str(temp[4]).strip()
                #The above is the date_due split and then put into a list and then into different variables for use below.

                
                overdue_date = datetime.strptime(overdue_date_list, '%Y-%m-%d')
                current_date = datetime.today()

            # #These variables* (lists) above will be used to help gather and use the info from the tasks.txt file.
            users = users.split()
            num_task_user_total_list = []
            Assigned_to = []
            completed = []
            num_task_user_incomplete_list = []
            num_task_user_over_list = []
                    
            for user in users:
                user_tasks = 0
                user_completed = 0
                user_uncompleted = 0
                user_overdue = 0

                for line in tasks_info:

                    if user in line:
                        user_tasks += 1
                        if ("Yes" in line):
                            user_completed += 1
                        if ("No" in line):
                            user_uncompleted += 1
                        if ("No" in line) and (str(current_date) > str(overdue_date)):
                            user_overdue += 1



              
                percentage_user_tasks = (100 / amount_tasks) * user_tasks
                percentage_user_completed = (100 / user_tasks) * user_completed
                percentage_user_uncompleted = (100 / user_tasks) * user_uncompleted
                percentage_user_overdue = (100 / user_tasks) * user_overdue


                num_task_user_total_list.append(user_tasks)
                Assigned_to.append(percentage_user_tasks)
                completed.append(percentage_user_completed)
                num_task_user_incomplete_list.append(percentage_user_uncompleted)
                num_task_user_over_list.append(percentage_user_overdue)

            each_users_output = []
            count = 0
            users_reported = ""
            for user in users:
                

                if user not in users_reported:
                    
                    each_users_output.append(
                        "\n"
                        + user
                        + "\nTasks assigned\t\t\t:"
                        + str(num_task_user_total_list[count])
                        + "\nTasks assigned of total tasks\t:"
                        + str(round(Assigned_to[count], 1))
                        + "%\nTasks assigned completed\t:"
                        + str(round(completed[count], 1))
                        + "%\nTasks assigned incomplete\t:"
                        + str(round(num_task_user_incomplete_list[count], 1))
                        + "%\nTasks assigned overdue\t\t:"
                        + str(round(num_task_user_over_list[count], 1))
                        + "%\n"
                    )
                    users_reported += user + " "
                
                count += 1


            user_overview.write(f"The total amount of Tasks is {amount_tasks}\n")
            user_overview.writelines(each_users_output)

    tasks.close()
    user_overview.close()


# gen_report()


def display_stats():

    with open ('task_overview.txt', 'r') as task_overview:

        task_data = task_overview.read()
        print("")
        print("The statistics for tasks are:")
        print("")
        print(task_data)

    task_overview.close()

    print("*" * 30)
    print("*" * 30)
    print("*" * 30)

    with open ('user_overview.txt', 'r') as user_overview:

        user_data = user_overview.read()
        print("")
        print("The statistics for users are:")
        print("")
        print(user_data)

    user_overview.close()

    print("<>" * 30)
    print("<>" * 30)

    # print(words1[0] + "\n" +(words1[1])


# this login section was accomplished with the help of Wihan.pre from the hyperion discord
login = False
with open("user.txt", "r") as login_details:
    login_details = login_details.read()
# this loop will help reapeat the questions if the wrong names or passwords are entered
while login == False:
    username = input("enter details: ")
    password = input("enter password: ")
    print("=" * 50)
    print("=" * 50)
    print("=" * 50)
    # combining the 2 variables into one will make it simpler to read and understand in the code
    user_login = username + "," + password

    # the "in" key word will help to look into the txt files for the passwords and users
    if user_login in login_details:
        print("welcome back " + username)
        # breaking at this point will help to move on from the while loop and unto the menu
        login = True
    else:
        print("Incorrect credentials. Please try again.")
# the continue key word will keep the user in the loop till they enter the correct credentials
# continue


# this is the menu
# The while loop helps to ensure that the menu will continue to loop unless the user enters 'e' for exit
while login:
    print("Please select one of the following options: ")
    # if the user is the admin,they will be granted access to more features
    if username == "admin":
        options = input(
            " r - register User \n a - add task \n va - view all tasks \n vm - view my tasks \n ds - display statistics\n gr - generate reports\n e - exit: \n"
        )
    else:
        options = input(
            " a - add task \n va - view all tasks \n vm - view my tasks\n e - exit: \n"
        )

    print("=" * 50)
    print("=" * 50)
    print("=" * 50)
    # these options help to end off the function we created at the top of the code
    if options == "r":
        reg_user()
    if options == "a":
        add_task()
    if options == "va":
        view_all()
    if options == "vm":
        view_mine()
    if options == "gr":
        gen_report()
    if options == "ds":
        display_stats()
    if options == "e":
        print("You have chosen to end this program.\nThank you and have a good day.")
        # exit() will help to terminate the program, https://pythonguides.com/python-exit-command/
        login = False

password = []
