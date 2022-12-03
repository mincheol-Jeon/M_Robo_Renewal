import pymysql
import mysql.connector
import json
import pandas as pd

f  = open("config.json")
config = json.load(f)

def get_db_connection():
    connection = pymysql.connect(
        host = config['db']['host'],
        user = config['db']['user'],
        database = config['db']['database'],
        port = 3306,
        password = config['db']['password'],   
        autocommit = False
    )
    return connection

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('select * from cj;')
col = cursor.description
col_list = [col[i][0] for i in range(len(col))]
df = pd.DataFrame(cursor.fetchall(),columns = col_list)
print('Test')
