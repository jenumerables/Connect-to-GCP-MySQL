# Create Google Cloud SQL instance
# Named myfirstdatabase23

import mysql.connector

connect = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database="student"
)
# end connection details ###
my_cursor = my_connect.cursor()

my_cursor.execute("SELECT * FROM student")
my_result = my_cursor.fetchone()
while my_result is not None:
  print(my_result)
  my_result = my_cursor.fetchone()