import pymysql
import mysql.connector
import json
f  = open("config.json")
config = json.load(f)

def get_db_connection():
    pymysql.connect(
        host = config['db']['host'],
        user = config['db']['user'],
        database = config['db']['database'],
        port = '3306',
        password = config['db']['password'],   
        autocommit = False
    )