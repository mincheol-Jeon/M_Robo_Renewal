import pymysql
import mysql.connector
import json
import pandas as pd

def get_db_config():
    f  = open("config.json")
    config_json = json.load(f)
    
    return config_json

def get_db_connection(config):
    connection = pymysql.connect(
        host = config['db']['host'],
        user = config['db']['user'],
        database = config['db']['database'],
        port = config['db']['port'],
        password = config['db']['password'],   
        autocommit = False
    )
    return connection

# conn = get_db_connection()
# cursor = conn.cursor()
# cursor.execute('select * from cj;')
# col = cursor.description
# col_list = [col[i][0] for i in range(len(col))]
# df = pd.DataFrame(cursor.fetchall(),columns = col_list)
# print('Test')
