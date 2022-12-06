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

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello Flask!'
    
app.run(host='0.0.0.0',port=50)