from unittest.mock import patch
from networkx import NetworkXError
import pytest
import json
import os
from startingConfigFile import makeJSONFile, visualisationGraphs

@pytest.fixture(scope="session", autouse=True)
def before_module():
    # Create each testing JSON file
    data = [{"n": 4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}, {"n": 4, "starting-graph": "illegal", "red-graph": "illegal", "blue-graph": "illegal", "threadnumber": 1, "starting-player": 1, "bias": 0}, 
        {"n": "four", "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber":"one", "starting-player": "one", "bias": "zero"}, 
        {"n": -4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": -1, "starting-player": -1, "bias": -1}, 
        {"starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}]
    file = ["testStartingFile.json", "testStartingFileIllegalGraph.json", "testStartingFileIllegalIntType.json", "testStartingFileIllegalIntValue.json", "testStartingFileIllegalMissing.json"]
    for i in range(5):
        name_file = file[i]
        myJSON = json.dumps(data[i])
        with open(name_file, "w") as f:
            f.write(myJSON)
    # Run tests
    yield
    # Delete all testing JSON files 
    os.system('python3 deletion')


def test_makeJSONFile():
    makeJSONFile(
        n=4,
        starting_graph="C~",
        red_graph="C?",
        blue_graph="C?",
        thread_number=1,
        start_player_In= "red",
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
    # testStartingFileIllegalGraph.json
    # {"n": 4, "starting-graph": "illegal", "red-graph": "illegal", "blue-graph": "illegal", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with pytest.raises(NetworkXError):
        visualisationGraphs("testStartingFileIllegalGraph.json")


def test_visualisationGraphs_bestand_ontbreekt():
    with pytest.raises(FileNotFoundError):
        visualisationGraphs("/bestaat/niet.json")

os.system("python3 deletion")