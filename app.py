from flask import Flask
from flask_cors import CORS

import beginnen
import felixfile

app = Flask(__name__)
CORS(app)

@app.route("/vakantie")
def vakantie():
    return "<p>De vakantie gaat naar:</p>" + beginnen.database('abc')

@app.route("/abc/<hoi>")
def hello_world(hoi):
    return "<p>Hello, World!</p>" + hoi

@app.route("/test")
def test_page():
    return beginnen.mijnmethode()

@app.route("/dieren")
def databaseDieren():
    return beginnen.database("kip")

@app.route("/zoeken/<dier>")
def databaseZoeken(dier):
    return beginnen.database(dier)

@app.route("/felix/<gegeven>")
def methodeFelix(gegeven):
    return felixfile.methodenaam(gegeven)