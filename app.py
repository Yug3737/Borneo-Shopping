# file: app.py
# authors: Yug Patel
# last modified: 25 Nov 2024

import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

import MySQLdb.cursors

# import pymysql.cursors as cursors
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("BORNEO_SECRET_KEY")

app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new_buyer")
def new_buyer():
    return render_template("new_buyer.html")


@app.route("/new_seller")
def new_seller():
    return render_template("new_seller.html")


@app.route("/register_new_seller")
def register_new_seller():
    pass


@app.route("/register_new_buyer")
def register_new_buyer():
    pass


if __name__ == "__main__":
    app.run()
