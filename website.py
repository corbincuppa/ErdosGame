from makeGraphsFromHistory import makeGraphs
from startingConfigFile import makeJSONFile, writeHistory
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.before_request
def startup():
    # Make the graphs of the latest game
    makeGraphs()
    # From stacksoverflow
    app.before_request_funcs[None].remove(startup)
    startup()


@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/running_solver', methods=['POST', 'GET'])
def running_solver():
    order        =    request.form['order'];
    startGraph   =    request.form['startGraph'];
    redGraph     =    request.form['redGraph'];   
    blueGraph    =    request.form['blueGraph'];
    threads      =    request.form['threads'];
    startPlayer  =    request.form['start_player'];
    bias         =    request.form['bias'];
    os.system("python3 deletion")
    makeJSONFile(order, startGraph, redGraph, blueGraph, threads, startPlayer, bias)
    writeHistory("startingFile.json")
    makeGraphs()
    return redirect('/index')

    