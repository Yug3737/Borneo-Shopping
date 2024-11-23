# file: main.py
# authors: Yug Patel
# last modified: 22 Nov 2024

import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_passsword_hash
import MySQLdb.cursors
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("BORNEO_SECRET_KEY")

app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

@app.route('/')
def index_route():
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
