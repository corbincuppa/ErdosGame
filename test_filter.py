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

    # Controleer of het bestand bestaat
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
