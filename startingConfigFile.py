import os
import json
import re
import time
import networkx as nx
import matplotlib.pyplot as plt

def makeJSONFile(n, starting_graph, red_graph, blue_graph, thread_number, starting_player, bias):
    # Make the JSON format
    data = { "n" : n, 
            "starting-graph" : starting_graph,
            "red-graph" : red_graph, 
            "blue-graph" : blue_graph, 
            "threadnumber" : thread_number, 
            "starting-player" : starting_player,
            "bias" : bias
    }

    # Dump the data onto the JSON file
    myJSON = json.dumps(data)
    with open("startingFile.json", "x") as jsonfile:
        jsonfile.write(myJSON)
        print("Write successful!\n")
        print("Your JSON file is called 'startingFile.json'.\n")

def visualisationGraphs(file_name):
     # Open that file 
    with open(file_name, "r") as f:
        data = json.load(f)
        n = data["n"]
       

        # Make a new file which contains the given graphs in graph6 format
        with open("fileWithGraphString", "w") as g:
            g.write(data["starting-graph"]+"\n")
            g.write(data["red-graph"]+"\n")
            g.write(data["blue-graph"])

    graph = nx.read_graph6(g.name)

    # Generate each graph
    color = ["green", "red","blue"]
    title = ["Starting", "Red", "Blue"]
    clarifying_str = "\nYour graphs have been saved as .png files:\n"
    for i in range(3):
        fig, ax = plt.subplots()
        nx.draw(graph[i], node_color=color[i], edge_color=color[i], ax=ax)
        ax.set_title(f"{title[i]} graph")
        # Save each graph as a file 
        plt.savefig(f"{title[i]}Graph.png")
        clarifying_str += f"{title[i]}Graph.png\n"
    print(clarifying_str)    


    # Visualise each graph
    for i in range(3):
        os.system(f"open {title[i]}Graph.png")

def writeHistory(file_name):
    # Open the given file and parse the arguments to the software
    with open(file_name, "r") as f:
        data = json.load(f)
        n = data["n"]
        # Put the values in the JSON file into arguments
        starting_graph = data["starting-graph"]
        red_graph = data["red-graph"]
        blue_graph = data["blue-graph"]
        threads = data["threadnumber"]
        starting_player = data["starting-player"]
        bias = data["bias"]

        if not isinstance(n, (int)) or not isinstance(threads, (int)) or not isinstance(starting_player, (int)) or not isinstance(bias, (int)):
            raise TypeError()
        if n <= 0 or threads <= 0 or starting_player <= 0 or starting_player > 2 or bias < 0:
            raise ValueError()
        #if not is_graph6_format(starting_player) or not is_graph6_format(red_graph) or not is_graph6_format(blue_graph):
            #raise nx.NetworkXError
        
        # Call the solver function, save the terminal output path to a new file "pathToResult.txt"
        os.system(f"bash Erdos-Game-Generic.sh {n} {starting_graph} {red_graph} {blue_graph} {threads} {starting_player} {bias} >> pathToResult.txt")

        # make the current time of when the game was processed for history file making
        cur = time.ctime(time.time())

        # Return the results from the results.txt file
        with open("pathToResult.txt", "r") as h:
            path = h.readlines()
            path = path[0].replace("\n", "/results.txt")
            with open(str(path), "r") as i:
                result = i.readlines()
                print(result)

    # create the history file
    with open("history", "a") as j:
        # history file
        # date and time of when the game was processed
        # <timestamp>\t<base graph>\t<red graph>\t<blue graph>\t

        # player that wins
        win = result[-3].split(" ")
        win = win[-1].split("\n")
        win = win[0]
        win = int(win)
        if win > 10:
            winning_player = "red"
            score_red = win//11
            score_blue = win%11
        else:
            winning_player = "blue"
            # score
            score_red = win
            score_blue = win
        score = f"{score_red} - {score_blue}"

        # write the history of the game to the file
        j.write(f"{cur}\t{starting_graph}\t{red_graph}\t{blue_graph}\t{bias}\t{winning_player}\t{score}\n")








def user_friendly_solver():        
    # Ask if user wants to make a JSON file or not
    boolean_already_JSON = input("Do you already have a JSON file ready? [Y/n]\n")
    while boolean_already_JSON.upper() != "Y" and boolean_already_JSON.upper() != "N":
        print("\nThat is not an answer.\n")
        boolean_already_JSON = input("Do you already have a JSON file ready? [Y/n]\n")
            
    if boolean_already_JSON.upper() == "N":
        print("Then a JSON file will be made with the next given arguments:")
        # Ask for the given arguments to be put in the JSON config file
        n_In = int(input("What is the order of the starting graph?\n"))
        starting_graph = input("What is the starting graph in graph6 format?\n")
        red_graph_In = input("What is the graph6 format of the graph with which red starts?\n")
        blue_graph_In = input("What is the graph6 format of the graph with which blue starts?\n")
        thread_number_In = int(input("How many threads are allowed?\n"))
        start_player_In = input("Which colour starts?\n")
        # game bias, ask how many extra edges blue colours.
        bias = int(input("For each edge that red colours, how many extra edges can blue colour? [0 if they colour equally]\n"))

        # Change the variable value based on the colour chosen
        start_player = 0
        if start_player_In.upper() == "BLUE":
            start_player = 2
        elif start_player_In.upper() == "RED":
            start_player = 1

        makeJSONFile(n_In, starting_graph, red_graph_In, blue_graph_In, thread_number_In, start_player, bias)

        # If the user doesn't already have one, make the file_name variable the created JSON file
        file_name = "startingFile.json"

    # If the user has a JSON file, then ask for its name
    elif boolean_already_JSON.upper() == "Y":
            # Ask for the name of the JSON file
            file_name = input("What is the name of your JSON file?\n")

    # Ask for optional visualisation
    boolean_visualisation = input("Do you want to visualise the given graphs? [Y/n]\n")
    while boolean_visualisation.upper() != "Y" and boolean_visualisation.upper() != "N":
        print("\nThat is not an answer.\n")
        boolean_visualisation = input("Do you want to visualise the given graphs? [Y/n]\n")

    if boolean_visualisation.upper() == "Y":
        visualisationGraphs(file_name)

    elif boolean_visualisation.upper() == "NO":
        print("\nOK.\nHere are the results of the graph solver:")

    writeHistory(file_name)

#user_friendly_solver()