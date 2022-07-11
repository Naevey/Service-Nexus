
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import json, requests
from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL
import mySQLdb.cursors
import re

# create a Flask instance
app = Flask(__name__)

app.secret_key = 'service-NEXUS-a72387as349sjidla02'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'service-nexus'
app.config['MYSQL_PASSWORD'] = 'NEXUS-TEMP'
app.config['MYSQL_DB'] = 'nexus'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("/foundation/home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():



@app.route('/aboutdylan/')
def aboutdylan():
    return render_template("aboutdylan.html")

@app.route('/aboutritvik/')
def aboutritvik():
    return render_template("aboutritvik.html")

@app.route('/aboutadi/')
def aboutadi():
    return render_template("aboutadi.html")

@app.route('/aboutjean/')
def aboutjean():
    return render_template("aboutjean.html")

@app.route('/aboutsohan/')
def aboutsohan():
    return render_template("aboutsohan.html")

@app.route('/aboutkurtis/')
def aboutkurtis():
    return render_template("aboutkurtis.html")

@app.route('/servicesearch/')
def servicesearch():
    return render_template("servicesearch.html")

if __name__ == "__main__":
    app.run(debug=True, port=777)