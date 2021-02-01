# mysql-data-transfer
Download and install the XAMPP free software version 8.0.1

Go to the XAMPP installation folder and run xampp_control

start the MYSQL, Apache and browse localhost on your web browser and click phpMyadmin

Install dependencies such as pandas and mysql.connector using

pip install pandas

pip install mysql-connector-python

Please give the task_data.csv corect path in the main.py

otherwise keep it in same folder

main.py will create new database with a given name and table. 

Then all the task_data.csv transfer to the database table  

which is available at  http://localhost/phpmyadmin/

then click taskdatabase --> task

If you run several time this main.py file every time it

will erase and create new database and table in order to avoid

conflict.

Output:

Successfully connected to the localhost

taskdatabase is created.....

You're connected to database:  ('taskdatabase',)

Creating table....

task table is created....

Data Transferring......: 0

Data Transferring......: 1

Data Transferring......: 2

Data Transferring......: 3

..........................

..........................

..........................



