from flask import render_template, request, Flask
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import json, requests

# create a Flask instance
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("Home.html")


@app.route('/AboutDylan/')
def AboutDylan():
    return render_template("AboutDylan.html")

@app.route('/AboutRitvik/')
def AboutRitvik():
    return render_template("AboutRitvik.html")

@app.route('/AboutAdi/')
def AboutAdi():
    return render_template("AboutAdi.html")

@app.route('/AboutJean/')
def AboutJean():
    return render_template("AboutJean.html")

@app.route('/AboutSohan/')
def AboutSohan():
    return render_template("AboutSohan.html")

@app.route('/AboutKurtis/')
def AboutKurtis():
    return render_template("AboutKurtis.html")

if __name__ == "__main__":
    app.run(debug=True, port=777)