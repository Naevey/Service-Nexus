from flask import render_template, request, Flask
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import json, requests

# create a Flask instance
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("Home.html")


@app.route('/AboutUs/')
def AboutUs():
    return render_template("AboutUs.html")

if __name__ == "__main__":
    app.run(debug=True, port=777)