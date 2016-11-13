import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from os.path import join, dirname
import json



def main(config):
    output = []
    db = mysql.connector.Connect(**config)
    curprep = db.cursor(cursor_class=MySQLCursorPrepared)
    cur = db.cursor()
    cur.execute("SELECT * FROM free_response")
    for column in cur:
        with open ('freeresponse.txt','w') as file:
            file.write(str(column))
            file.write('\n')

if __name__ == '__main__':

    config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'udest',
        'user': 'root',
        'password': '',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }

    out = main(config)
    #print('\n'.join(out))
  