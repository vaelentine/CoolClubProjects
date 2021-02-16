from Typewriter.Typewriter import Typewriter
import sqlite3
from time import strftime, localtime

# check time. Is it morning? Greet based on time of day and day of week
# query user first time per day if would like to do some daily logging of goals for day
# query user near end of day if would like to log accomplishments for day
# query user if they would like to add any tasks to daily task goals
# log tasks, goals, values, activities
# ask user what they would like to do?

# connect/create the inital db file
connection = sqlite3.connect('user_data.db')
# interaction with the db
cursor = connection.cursor()

t = Typewriter()

t.print("good (whatever time of day it is now), (user-Maggie).\n")
t.print("would you like to make a new daily log?")
daily_log_now = input("y/N?" )
if daily_log_now.lower() == 'y':
    t.print("daily log not yet supported.")

t.print("Would you like to try and accomplish a task?")
give_task = input("y/N?" )

if give_task.lower() == 'y':
    t.print("giving tasks is not yet supported.")

t.print("Would you like to log some new tasks?")
log_new = input("y/N?" )
if log_new.lower() == 'y':
    t.print("What is something you'd like to accomplish or have been putting off?")
    logged = False
    while not logged:
            task_name = input('something you could do: ')
            t.print(f'you answered: {task_name}. is this correct?')
            correct = input('y/N' )
            if correct.lower() == 'y':
                logged = True
            else:
                t.print("ok. try again.")
    t.print("add some more description.")
    logged = False
    while not logged:
        task_description = input('more info: ')
        t.print(f'you answered: {task_description}. is this correct?')
        correct = input('y/N')
        if correct.lower() == 'y':
            logged = True
        else:
            t.print("ok. try again.")
    t.print("what type of task is this?")
    types = ['task', 'activity', 'goal']
    chosen = False
    while not chosen:
        t.print(f'available types are')
        for type in types:
            t.print(f'{types.index(type) + 1}. {type}. ')
        task_type = input("\nYour choice?  ")
        try:
            task_type = types[int(task_type) - 1]
        except:
            t.clear()
            print(f"I'm sorry. {task_type} is not a valid choice.")
        t.print(f"You chose {task_type}. Is this correct?")
        correct = input('y/N')
        if correct.lower() == 'y':
            chosen = True

    t.print("what is the closest estimate for how long this will take?")
    times = [15, 30, 45, 60]
    chosen = False
    while not chosen:
        t.print(f'choices are:')
        for time in times:
            t.print(f'{times.index(time) + 1}. Around {time} minutes. ')
        minutes_estimate = input("\nYour choice?  ")
        try:
            minutes_estimate = times[int(minutes_estimate) - 1]
        except:
            t.clear()
            print(f"I'm sorry. {minutes_estimate} is not a valid choice.")
        t.print(f"You chose {minutes_estimate}. Is this correct?")
        correct = input('y/N')
        if correct.lower() == 'y':
            chosen = True

    # log this into the db
    curr_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    completed = False
    date_comp = None

    cursor.execute(f'''INSERT INTO
        tasks(
            task_name,
            task_description,
            date_created,
            task_type,
            minutes_estimate,
            completed,
            date_completed
        )
    VALUES
        ('{task_name}', '{task_description}', '{curr_time}', '{task_type}', '{minutes_estimate}', '{completed}', '{date_comp}')''')
    connection.commit()

t.print("Would you like to see all of the tasks?")
see_all = input("y/N? ")
if see_all.lower() == 'y':
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print('\n')

t.print('be seeing you.')
