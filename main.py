
from transferData import data_transfer

# creating object of class data_transfer

task = data_transfer('sql_data_transfer/task_data.csv', 'localhost', 'root', '', 'taskdatabase', 'task')
# read csv file
task.read_csv()
# Get connected with host
task.connect_host()
# Create new database
task.create_newdb()
# create new table in a given database
task.create_newtb()
# transfer data to the table
task.sql_transfer()
