import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

[program, file_name, extension] = sys.argv

def listConverter(list):
    #turns a list with strings into matrix format
    result = []
    for row in list:
        row = row.strip()  
        new_row = []
        for char in row:
            if char == 'n':
                new_row.append(0)
            else:  
                new_row.append(int(char))
        result.append(new_row)
    return result

def exportingEndGameGraphs(file_name, extension):
    #the size of the matrix
    with open(file_name, "r") as f:
        data = json.load(f)
        n = data["n"]
    #extracting the end-game matrices 
    with open("pathToResult.txt", "r") as h:
        path = h.readlines()
        path = path[0].replace("\n", "/results.txt")
        with open(str(path), "r") as i:
            result = i.readlines()

    endGameRed = result[2:(n+2)]
    endGameRed = listConverter(endGameRed)
    endGameRed = nx.from_numpy_array(np.matrix(endGameRed))
    endGameBlue = result [(n+3): (2*n + 3)]
    endGameBlue = listConverter(endGameBlue)
    endGameBlue = nx.from_numpy_array(np.matrix(endGameBlue))

    
    fig, ax = plt.subplots()
    nx.draw(endGameRed, node_color="red", edge_color="red", ax=ax)
    ax.set_title(f"End game Alice graph")
    plt.savefig(f"EndGameAliceGraph.{extension}")

    fig, ax = plt.subplots()
    nx.draw(endGameBlue, node_color="blue", edge_color="blue", ax=ax)
    ax.set_title(f"End game Bob graph")
    plt.savefig(f"EndGameBobGraph.{extension}")

exportingEndGameGraphs(file_name, extension)