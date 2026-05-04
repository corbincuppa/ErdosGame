import pytest
#from startingConfigFile import user_friendly_solver
from automatedArgs import K_4

def test_parsed_arguments(capsys):
    K_4()
    # assert that parsed arguments are the given arguments
    captured = capsys.readouterr()
    #assert captured.out == "Do you already have a JSON file ready? [Y/n]\nThen a JSON file will be made with the next given arguments:\nWhat is the order of the starting graph?\nWhat is the starting graph in graph6 format?\n\nWhat is the graph6 format of the graph with which red starts?\nWhat is the graph6 format of the graph with which blue starts?\nHow many threads are allowed?\nWhich colour starts?\nWrite successful!\nYour JSON file is called 'startingFile.json'.\nDo you want to visualise the given graphs? [Y/n]\n\nYour graphs have been saved as .png files:\nStartingGraph.png\nRedGraph.png\nBlueGraph.png\n\n['The best graph is:\n', 'Color 1:\n', 'n010\n', '0n00\n', '10n0\n', '000n\n', 'Color 2:\n', 'n000\n', '0n00\n', '00n0\n', '000n\n', 'With fitness clique: 2\n', 'With fitness vertex capture: 2\n', 'With fitness max degree: 2\n']\n\nHistory of game saved.\n"
    assert captured.out == ['The best graph is:\n', 'Color 1:\n', 'n010\n', '0n00\n', '10n0\n', '000n\n', 'Color 2:\n', 'n000\n', '0n00\n', '00n0\n', '000n\n', 'With fitness clique: 2\n', 'With fitness vertex capture: 2\n', 'With fitness max degree: 2\n']
    
