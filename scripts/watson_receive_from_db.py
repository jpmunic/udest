import mysql.connector
import send_to_db
from os.path import join, dirname
import json



def main(config):
    output = []
    db = mysql.connector.Connect(**config)
    cursor = db.cursor()
    stmts = ["SELECT * FROM top_cities(cities)"]
    with open ('top_cities.txt','w') as file:
	for item in suggestion_list:
		file.write(str(item))
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

    #out = main(config)
    #print('\n'.join(out))
    send_to_db.main(config)