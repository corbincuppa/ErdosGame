# edge-colouring-games

This repository contains a more user friendly solver for a graph-colouring game designed by Erdös which is created for the article "On edge-colouring-games by Erdös, and Bensail and Mc Inerney".

The latest version of this program can be obtained from <https://github.com/ErdosGame>.

This program offers a more user friendly interface for the erdos-colouring-games(https://github.com/Algorithmic-Graph-Theory-Group/edge-colouring-games) solver. Optionally the specified graphs and end graphs of played games can be visualised.

### Installation

Make sure you clone this repository into your root directory.

This requires a working shell and `make`.

- Download, extract and configure [`nauty`](https://pallini.di.uniroma1.it/) in a folder nauty2_9_3.
- Copy this folder into the repository folder.
- Configure and compile the nauty libraries for multithreading using: `cd nauty2_9_3` `./configure --enable-tls` and `make`.
- Compile using: 
	* `cd -` and `make all-64bit` to create a binary for the 64 bit version


### Usage of user_friendly_solver


Usage: `python3 -c 'from startingConfigFile import user_friendly_solver; user_friendly_solver()'`

This programs makes use of JSON files. If you already have a JSON file in the following format:
```
{
	"n" : n
	"starting-graph" : starting_graph,
	"red-graph" : red_graph, 
	"blue-graph" : blue_graph, 
	"threadnumber" : thread_number, 
	"starting-player" : starting_player,
	"bias" : bias
}
```
Then give the name of that JSON file to be parsed into the solver. If not, the program will make a JSON file for you and automatically run the solver. You may also choose to visualise the graphs. These will be saved as '.png' files to your computer. 

### Examples
`function`
Explanation


### Verification

Lorem ipsum