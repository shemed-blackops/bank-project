import mysql.connector
import os.path


class DB:
    profile = {
        'host': 'localhost',
        'user': 'root',
        'password': '2uyDWuy/HW4dp+m'
    }

    def __init__(self):
        conn = mysql.connector.connect(
            host=DB.profile.get('host'),
            user=DB.profile.get('user'),
            password=DB.profile.get('password'),
        )

        c = conn.cursor()
        sql = 'SHOW DATABASES;'
        c.execute(sql)
        result = c.fetchall()
        for table in result:
            if 'bank' in table:
                print('Database found')



