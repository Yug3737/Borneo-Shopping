#! /usr/bin/python3
from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'Hello World'
       
app.run(host='localhost', port=5000)

