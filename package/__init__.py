import pymysql
import mysql.connector
import json
import pandas as pd
import os
from flask import Flask

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

def fetch(query,cursor,data_type = 'dataframe'):
    cursor.execute(query)

    if data_type == 'dataframe':
        
        col = cursor.description
        col_list = [col[i][0] for i in range(len(col))]
        res = pd.DataFrame(cursor.fetchall(),columns = col_list)
        
        return res
    
    if data_type == 'raw':
        res = cursor.fetchall()
        return str(res)
        
    

app = Flask(__name__)
conn = get_db_connection(get_db_config())
cursor = conn.cursor()

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/test')
def test_page():
    param = input()
    res = fetch(query = ''' 
                            select corp_name, corp_code, stock_code, url, rcept_dt
                            from tmp 
                            where corp_name = "{}" 
                            order by rcept_dt 
                            limit 5;
                        '''.format(param),
                cursor = cursor,
                data_type = 'raw')
    return res
    
app.run(host='0.0.0.0',port=50)