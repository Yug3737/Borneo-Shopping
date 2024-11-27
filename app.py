# file: app.py
# authors: Yug Patel
# last modified: 25 Nov 2024

import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors

app = Flask(__name__)

input_file = '.env'
variables = {}
with open(input_file, 'r') as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            variables[key] = value

BORNEO_SECRET_KEY = variables['BORNEO_SECRET_KEY']
MYSQL_HOST = variables['MYSQL_HOST']
MYSQL_USER = variables['MYSQL_USER']
MYSQL_DB = variables['MYSQL_DB']


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

@app.route("/buyer_login")
def buyer_login():
    return render_template("buyer_login.html")

@app.route("/logged_in_buyer")
def logged_in_buyer():
    pass

@app.route("/seller_login")
def seller_login():
    return render_template("seller_login.html")

@app.route("/logged_in_seller")
def logged_in_seller():
    pass



if __name__ == "__main__":
    app.run(port=3103)

# Comments
# Wanna be able to buy, if click buy, 
# before buying, login page, after purchse, give success.html
# 