import mysql.connector
from mysql.connector import Error
from read_config import read_config


class Database:
    db_config = read_config()

    def __init__(self):
        self.conn = None
        self.host = Database.db_config['mysql']['host']
        self.user = Database.db_config['mysql']['user']
        self.password = Database.db_config['mysql']['password']
        self.database = Database.db_config['mysql']['database']

        # connect()

    # Connecting to database
    def connect(self):
        # Create connection
        try:

            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)

            if self.conn.is_connected():
                return self.conn
        except Error as e:
            print(e)
