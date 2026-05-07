from makeGraphsFromHistory import makeGraphs
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.before_request
def before_request():
    makeGraphs()

@app.route('/index')
def index():
    return render_template("index.html")