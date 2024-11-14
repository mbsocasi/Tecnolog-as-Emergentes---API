import os
import mysql.connector
from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB'),
        port=os.getenv('MYSQL_PORT')
    )
