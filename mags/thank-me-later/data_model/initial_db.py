"""
This file creates the database and adds the initial table with columns

"""
#
import sqlite3
from time import strftime, localtime
# connect/create the inital db file
connection = sqlite3.connect('../user_data.db')
# interaction with the db
cursor = connection.cursor()

# execution commands in SQL
cursor.execute('''CREATE TABLE tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             task_name  varchar(50) NOT NULL,
             task_description varchar(200),
             date_created varchar(20) NOT NULL,
             completed BOOLEAN,
             date_completed TEXT,
             task_type varchar(50) NOT NULL,
             minutes_estimate INTEGER)''')

# curr_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
# task_name = 'testName'
# task_desc = 'testDesc'
# task_type = 'task'
# completed = False
# date_comp = None
#
# cursor.execute(f'''INSERT INTO
#     tasks(
#         task_name,
#         task_description,
#         date_created,
#         task_type
#     )
# VALUES
#     ('{task_name}', '{task_desc}', '{curr_time}', '{task_type}')''')
#
# connection.commit()  #save yo changes
# connection.close()