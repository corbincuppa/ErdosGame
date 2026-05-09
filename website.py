from makeGraphsFromHistory import makeGraphs
from startingConfigFile import makeJSONFile, writeHistory, exportingEndGameGraphs
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.before_request
def startup():
    # Make the graphs of the latest game
    makeGraphs()
    # From stacksoverflow
    app.before_request_funcs[None].remove(startup)


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
    makeJSONFile(int(order), startGraph, redGraph, blueGraph, int(threads), startPlayer,int(bias))
    path = os.path.expanduser("~/ErdosGame")
    writeHistory(path, "startingFile.json")
    makeGraphs()
    exportingEndGameGraphs("startingFile.json", "png")
    os.system("mv EndGameAliceGraph.png ~/ErdosGame/static/images/")
    os.system("mv EndGameBobGraph.png ~/ErdosGame/static/images/")
    return redirect('/index')