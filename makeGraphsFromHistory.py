import os
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def makeGraphs():
    # Open the history.txt file and get the results of the last game
    with open("history.txt") as h:
        last_game = h.readlines()[-1]
        # split the results
        last_game = last_game.split("\t")

    # Get each graph
    start_graph_str = last_game[-6]
    red_graph_str = last_game[-5]
    blue_graph_str = last_game[-4]
    # Write each graphto a new line of a temp file so networkx can read multiple
    with open("temp.txt", "w") as t:
        t.write(start_graph_str+"\n")
        t.write(red_graph_str+"\n")
        t.write(blue_graph_str)

    graph = nx.read_graph6("temp.txt")
    
    # Delete the temporary file, it is not needed anymore
    os.system("rm temp.txt")

    # Generate each graph
    color = ["green", "red","blue"]
    title = ["Starting", "Red", "Blue"]
    for i in range(3):
        fig,ax = plt.subplots()
        # Each graph has its respective colour 
        nx.draw(graph[i], node_color=color[i], edge_color=color[i], ax=ax)
        ax.set_title(f"{title[i]} graph")
        # Save each graph as a file 
        plt.savefig(f"static/images/{title[i]}Graph.png") 
        plt.close()   
