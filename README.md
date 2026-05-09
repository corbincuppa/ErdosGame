# ErdosGame

This repository contains a more user friendly solver for a graph-colouring game designed by Erdös which is created for the article "On edge-colouring-games by Erdös, and Bensail and Mc Inerney".

The latest version of this program can be obtained from <https://github.com/ErdosGame>.

This program offers a more user friendly interface for the [`erdos-colouring-games`](https://github.com/Algorithmic-Graph-Theory-Group/edge-colouring-games) solver. Optionally the specified graphs and end graphs of played games can be visualised. The program also holds history of the played games with the time of when the game was processed, given starting graph, red graph and blue graph, bias, winning player and final score.

### Installation

Make sure you clone this repository into your root directory.

This requires a working shell and `make`.

- Download, extract and configure [`nauty`](https://pallini.di.uniroma1.it/) in a folder nauty2_9_3.
- Copy this folder into the repository folder.
- Configure and compile the nauty libraries for multithreading using: `cd nauty2_9_3` `./configure --enable-tls` and `make`.
- Compile using: 
	* `cd -` and `make all-64bit` to create a binary for the 64 bit version


### Usage of user_friendly_solver


Usage: `python3 -c 'from startingConfigFile import user_friendly_solver; user_friendly_solver()' `

This programs makes use of JSON files. If you already have a JSON file in the following format:
```
{
	"n" : 				the order of the graph on which the game is played
	"starting-graph" : 	the starting graph in graph6 format
	"red-graph" : 		the start graph of the red player (Alice) in graph6 format
	"blue-graph" : 		the start graph of the blue player (Bob) in graph6 format
	"threadnumber" : 	the number of threads
	"starting-player" : 	the player who starts (red or blue)
	"bias" : 			blue can select # more edges than red in its turn
}
```
Then input the name of that JSON file to be parsed into the solver. If not, the program will make a JSON file for you and automatically run the solver. You may also choose to visualise the graphs. These will be saved as '.png' files to your computer and shown by the program. 

### Usage of makeJSONFile

Usage: `python3 -c 'from startingConfigFile import makeJSONFile ; makeJSONFile(n, starting_graph, red_graph, blue_graph, thread_number, starting_player, bias)' `

```
The arguments have the same definition as the elements in the JSON file format above. 
See "Usage of user_friendly_solver".
```

### Usage of visualisationGraphs

Usage: `python3 -c 'from startingConfigFile import visualisationGraphs; visualisationGraphs(file_name)' `
```
file_name				the name of the JSON file containing the given format
```
This program takes the given JSON file and saves the starting, red and blue graphs as `.png` files in the `~/ErdosGame` directory.


### Usage of writeHistory

Usage: `python3 -c 'from startingConfigFile import writeHistory; writeHistory(file_name)' `

```
file_name				the name of the JSON file containing the given format
```
This program runs the solver given the arguments in the JSON file and saves a history of the played game containing the time of when the game was processed, the starting, red and blue graphs, bias and final score. This is saved to `~/ErdosGame/history.txt`

### Usage of restoreBackup
Usage: `python3 restoreBackup`

This program will show all possible backups, which are saved hourly. It then asks which history backup file you would like to restore to. The history.txt is then overwritten by the chosen backup.

### Usage of deletion

Usage: `python3 deletion`

If you wish to delete all generated files by the program, run the deletion script. This will delete the following files:
```
StartGraph.png
RedGraph.png
fileWithGraphString
pathToResult.txt
temp.txt
startingFile.json
```
