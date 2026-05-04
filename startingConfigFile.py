import os
import json
import time
import networkx as nx
import matplotlib.pyplot as plt


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
        start_player = input("Which colour starts?\n")

        # Change the variable value based on the colour chosen
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
        with open("startingFile.json", "x") as jsonfile:
            jsonfile.write(myJSON)
            print("Write successful!\n")
            print("Your JSON file is called 'startingFile.json'.\n")

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
        # Open that file 
        with open(file_name, "r") as f:
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

    elif boolean_visualisation.upper() == "NO":
        print("\nOK.\nHere are the results of the graph solver:")

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
        print("\nHistory of game saved.\n")

user_friendly_solver()