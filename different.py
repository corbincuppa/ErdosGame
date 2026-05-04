import os
import json
import time
import networkx as nx
import matplotlib.pyplot as plt


def what(json_file_name, n_In, starting_graph, red_graph_In, blue_graph_In, thread_number_In, start_player, boolean_visualisation):
    starting_player_In = 0
    if start_player.upper() == "BLUE":
        starting_player_In = 2
    elif start_player.upper() == "RED":
        starting_player_In = 1

    # Make the JSON format
    data = { "n" : n_In, 
            "starting-graph" : starting_graph,
            "red-graph" : red_graph_In, 
            "blue-graph" : blue_graph_In, 
            "threadnumber" : thread_number_In, 
            "starting-player" : starting_player_In
    }

    # Dump the data onto the JSON file
    myJSON = json.dumps(data)
    with open(json_file_name, "x") as jsonfile:
        jsonfile.write(myJSON)

    if boolean_visualisation.upper() == "Y":
        # Open that file 
        with open(json_file_name, "r") as f:
            data = json.load(f)
            n = data["n"]
        

            # Make a new file which contains the given graphs in graph6 format
            with open("fileWithGraphString", "x") as g:
                g.write(data["starting-graph"]+"\n")
                g.write(data["red-graph"]+"\n")
                g.write(data["blue-graph"])

        graph = nx.read_graph6(g.name)

        # Generate each graph
        color = ["green", "red","blue"]
        title = ["Starting", "Red", "Blue"]
        for i in range(3):
            fig, ax = plt.subplots()
            nx.draw(graph[i], node_color=color[i], edge_color=color[i], ax=ax)
            ax.set_title(f"{title[i]} graph")
            # Save each graph as a file 
            plt.savefig(f"{title[i]}Graph.png")

        # Visualise each graph
        for i in range(3):
            os.system(f"open {title[i]}Graph.png")

    # Open the given file and parse the arguments to the software
    with open(json_file_name, "r") as f:
        data = json.load(f)
        n = data["n"]
        # Put the values in the JSON file into arguments
        starting_graph = data["starting-graph"]
        red_graph = data["red-graph"]
        blue_graph = data["blue-graph"]
        threads = data["threadnumber"]
        starting_player = data["starting-player"]

        # Call the solver function, save the terminal output path to a new file "pathToResult.txt"
        os.system(f"bash Erdos-Game-Generic.sh {n} {starting_graph} {red_graph} {blue_graph} {threads} {starting_player} >> pathToResult.txt")

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

        # game bias, temporary
        bias = 0

        # player that wins
        win = result[-2].split(" ")
        win = win[-1].split("\n")
        win = win[0]
        win = int(win)
        if win > 10:
            winning_player = "red"
        else:
            winning_player = "blue"

        # final score, example
        score = "2 - 10"
        j.write(f"{cur}\t{starting_graph}\t{red_graph}\t{blue_graph}\t{bias}\t{winning_player}\t{score}\n")
