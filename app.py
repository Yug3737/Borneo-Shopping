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
MYSQL_PASSWORD = variables['MYSQL_PASSWORD']
MYSQL_DB = variables['MYSQL_DB']

app.config["MYSQL_HOST"] = MYSQL_HOST
app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB

mysql = MySQL(app)


@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name, price, ID from product")
    mysql.connection.commit()
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template("index.html", data=data)

@app.route("/product/<int:product_id>", methods=['GET'])
def view_product(product_id):
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM product WHERE ID = %s'
    cursor.execute(query, (product_id,))
    mysql.connection.commit()
    product_data = cursor.fetchone()
    print(product_data)
    cursor.close()
    return render_template('view_product.html', product=product_data)
    print(data)

@app.route("/<int:product_id>/choose_payment_method", methods=['GET', 'POST'])
def choose_payment_method(product_id):
    return render_template('choose_payment_method.html')

@app.route("/buy_product/<int:product_id>", methods=['GET', 'POST'])
def buy_product(product_id, buyer_id):
    cursor = mysql.connection.cursor()

    

@app.route("/new_buyer", methods= ['POST', 'GET'])
def new_buyer():
    return render_template("new_buyer.html")

@app.route("/register_new_buyer", methods= ['POST', 'GET'])
def register_new_buyer():
    if request.method == 'GET':
        return 'Please Fill the Form with necessary details.'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']

        # DATA VALIDATION
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO `buyer`(`name`, `address`, `phone_number`, `email`, `password`) VALUES (%s,%s,%s,%s,%s);'
        cursor.execute(query, (name, address, phone_number, email, password))
        mysql.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        print(data)
        return render_template('successful_buyer_registration.html', name=name)



@app.route("/new_seller")
def new_seller():
    return render_template("new_seller.html")


@app.route("/register_new_seller", methods=['GET', 'POST'])
def register_new_seller():
    if request.method == 'GET':
        return 'Please Fill the Form with necessary details.'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']

        # DATA VALIDATION
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO `seller`(`name`, `address`, `phone_number`, `email`, `password`) VALUES (%s,%s,%s,%s,%s);'
        cursor.execute(query, (name, address, phone_number, email, password))
        mysql.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return render_template('successful_seller_registration.html', name=name)


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