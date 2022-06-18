from flask import render_template, request
import requests
import json
from starter import app_starter
from algorithm import app_algorithm
from webapi import app_api
from dc_crud.app_crud import app_crud
from y2022 import app_y2022
from web.websiteSearch import websiteSearch
from __init__ import app

app.register_blueprint(app_starter)
app.register_blueprint(app_algorithm)
app.register_blueprint(app_api)
app.register_blueprint(app_crud)
app.register_blueprint(app_y2022)
app.register_blueprint(websiteSearch)

@app.route('/')
def index:
    return render_template("index.html")


@app.route('/AboutUs/')
def AboutUs
    return render_template("AboutUs.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8002)