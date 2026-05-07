import networkx as nx
import matplotlib.pyplot as plt

def makeGraphs():
    with open("history.txt") as h:
        last_game = h.readlines()[0]
        last_game = last_game.split("\t")

    start_graph_str = last_game[-6]
    red_graph_str = last_game[-5]
    blue_graph_str = last_game[-4]
    with open("temp.txt", "w") as t:
        t.write(start_graph_str+"\n")
        t.write(red_graph_str+"\n")
        t.write(blue_graph_str)

    graph = nx.read_graph6("temp.txt")

    # Generate each graph
    color = ["green", "red","blue"]
    title = ["Starting", "Red", "Blue"]
    clarifying_str = "\nYour graphs have been saved as .png files:\n"
    for i in range(3):
        fig, ax = plt.subplots()
        nx.draw(graph[i], node_color=color[i], edge_color=color[i], ax=ax)
        ax.set_title(f"{title[i]} graph")
        # Save each graph as a file 
        plt.savefig(f"static/images/{title[i]}Graph.png")    
