from unittest.mock import patch
from networkx import NetworkXError
import pytest
import json
import os
from startingConfigFile import makeJSONFile, visualisationGraphs

def test_makeJSONFile():
    makeJSONFile(
        n=4,
        starting_graph="C~",
        red_graph="C?",
        blue_graph="C?",
        thread_number=1,
        starting_player=1,
        bias=0
    )

    # Controleert of het bestand bestaat
    assert os.path.exists("startingFile.json")

    with open("startingFile.json", "r") as f:
        data = json.load(f)

    assert data["n"] == 4
    assert data["starting-graph"] == "C~"
    assert data["red-graph"] == "C?"
    assert data["blue-graph"] == "C?"
    assert data["threadnumber"] == 1
    assert data["starting-player"] == 1
    assert data["bias"] == 0


def test_visualisationGraphs():
    # testStartingFile.json
    # {"n": 4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}

    with patch("os.system") as mock_system:
        visualisationGraphs("testStartingFile.json")
        
        # Controleert of os.system 3 keer is aangeroepen (voor openen PNG's)
        assert mock_system.call_count == 3
    
        #fileWithGraphString ok opgesteld? 
        with open("fileWithGraphString", "r") as f:
            lines = f.readlines()
            assert lines[0] == "C~\n"
            assert lines[1] == "C?\n"
            assert lines[2] == "C?"

            # Controleert of het bestanden bestaat
            assert os.path.exists("StartingGraph.png")
            assert os.path.exists("RedGraph.png")
            assert os.path.exists("BlueGraph.png")



def test_visualisationGraphs_ongeldige_graph6():
    # testStartingFileOngeldig.json
    # {"n": 4, "starting-graph": "Ongeldig", "red-graph": "Ongeldig", "blue-graph": "Ongeldig", "threadnumber": 1, "starting-player": 1, "bias": 0}
    # networkx gooit een ValueError bij ongeldige graph6
    with  pytest.raises(NetworkXError):
        visualisationGraphs("testStartingFileOngeldig.json")


def test_visualisationGraphs_bestand_ontbreekt():
    with pytest.raises(FileNotFoundError):
        visualisationGraphs("/bestaat/niet.json")

