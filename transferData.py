
# imporing pandas, mysql
import pandas as pd
import mysql.connector as msql

class data_transfer(object):
    """
    This class will create new database, table and transfer the task_data.csv to the 
    table in the created database. Everytime it will check the existing database and table 
    with the given database and table name. If similar database and table exist in the server
    then this class delete and create the new table and database 
    """

    def __init__(self, csv_file, host, user, passwd, db_name, tb_name):

        """
        :param csv_file: csv file path
        :type csv_file: string
        :param host: database host name
        :type host: string
        :param user: user name
        :type user: string
        :param passwd: database password
        :type passwd: string
        :param db_name: new database neme
        :type db_name: string
        :param tb_name: new table name in a database
        :type tb_name: string

        """
        self.csv_file = csv_file 
        self.host = host
        self.user = user
        self.passwd = passwd 
        self.db_name = db_name
        self.tb_name = tb_name
        self.data = None
        self.conn = None
        self.cursor = None
        self.record = None
    
    def read_csv(self):

        """
        This methods checks the csv file reads successfully or not
        """
        try:
            self.data = pd.read_csv(self.csv_file, index_col=False)
            self.data.head()
            print('CSV reads successfully')

        except:
            raise Exception('Please use the correct csv file path')

    def connect_host(self):

        """
        This method establishes connecttion with the given host 
        """
        try:
            self.conn = msql.connect(host=self.host, user=self.user, password=self.passwd)
            print('Host connection succeeded')

        except:
            raise Exception("Error while connecting to MySQL database server")

    def create_newdb(self):

        """
        This method establishes connecttion with the given host and 
        craetes new database with the given name
        """
        drop_db = 'DROP DATABASE IF EXISTS' + ' ' + self.db_name
        create_db = 'CREATE DATABASE' + ' ' + self.db_name

        try:
            self.conn = msql.connect(host=self.host, user=self.user, password=self.passwd)
            self.cursor = self.conn.cursor()
            self.cursor.execute(drop_db)
            self.cursor.execute(create_db)
            print(self.db_name + " " + " is created.....")

        except:  
            raise Exception("Error while creating new database")

    def create_newtb(self):

        """
        This method establishes connecttion with the given host and database 
        then creates new table  
        """
        self.conn = msql.connect(host=self.host, database = self.db_name, user=self.user, password=self.passwd)
        drop_tb = 'DROP TABLE IF EXISTS' + ' ' + self.tb_name
        create_tb = "CREATE TABLE" + " " + self.tb_name + " " + "(id INT NOT NULL,\
                        timestamp TIMESTAMP(6) NOT NULL,\
                        temperature DOUBLE NOT NULL, \
                        duration VARCHAR(35) NOT NULL)"

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("select database()")
            self.record = self.cursor.fetchone()
            print("You're connected to database: ", self.record)
            self.cursor.execute(drop_tb)
            self.cursor.execute(create_tb)
            print(self.tb_name + " " + "table is created....")

        except:
            raise Exception("Error while creating new database table")

    def sql_transfer(self):

        """
        This method transfers the csv data to the newly created table in a
        given database
        """
        data_insert = "INSERT INTO" + " " + self.db_name + "." + self.tb_name + " " + "VALUES (%s,%s,%s,%s)"

        try:
            for i, row in self.data.iterrows():
                sql_data = data_insert
                self.cursor.execute(sql_data, tuple(row))
                print("Data Transferring......:", i)
                self.conn.commit()
            print("Data Transfer Completed")

        except:
            raise Exception("Data transfer failed")

  