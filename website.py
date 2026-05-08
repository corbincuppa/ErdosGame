from makeGraphsFromHistory import makeGraphs
from flask import Flask, render_template

app = Flask(__name__)

@app.before_request
def startup():
    # Make the graphs of the latest game
    makeGraphs()
    # From stacksoverflow

    startup()


@app.route('/index')
def index():
    return render_template("index.html")