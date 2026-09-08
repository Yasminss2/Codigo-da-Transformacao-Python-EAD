import sqlite3

conn = slqliite3.connect('all_sall_.db')
cursor = conn.cursor()


cursor.execute(

   '''
   CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCLEMENT,
      task_name TEXT NOT NULL,
      data_fish NUMBER NOT NULL,
      data_star NUMBER NOT NULL,
      tarefa_about STRING NOT NULL
   ) 
   ''' 
)
conn.commit