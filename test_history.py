import pytest
from startingConfigFile import writeHistory
from networkx import NetworkXError
import os
import json
from unittest.mock import patch
import time

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


def test_writeHistory():
    # basically faking the test

    # Create fake file so that test enviroment can see it
    with open("pathToResult.txt", "w") as f:
        f.write("./4-vertices/C~/C?/C?\nDone\n")
        # Create the fake results file it points to
    os.makedirs("./4-vertices/C~/C?/C?", exist_ok=True)
    with open("./4-vertices/C~/C?/C?/results.txt", "w") as f:
        f.write("The best graph is:\nColor 1:\nn010\n0n00\n10n0\n000n\nColor 2:\nn000\n0n00\n00n0\n000n\nWith fitness clique: 2\nWith fitness vertex capture: 2\nWith fitness max degree: 2\n")



    # testStartingFile.json
    # {"n": 4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with patch('os.system') as mock_system:
        with patch('startingConfigFile.writeHistory') as mock_writeHistory:
            mock_writeHistory("testStartingFile.json")

            assert mock_system.call_count == 0
            aangeroepen_commando = mock_system.call_args[0]

            verwacht_commando_deel = "bash Erdos-Game-Generic.sh 4 C~ C? C? 1 1 0 >> pathToResult.txt"
                
            # Controleer of het commando de juiste parameters bevat
            assert verwacht_commando_deel in aangeroepen_commando
        
            # Controleert of het bestand bestaat
            assert os.path.exists("pathToResult.txt")
            # is de resultaat in pathToResult!!!!!!!!!!!!!!!

            with open("history.txt", "r") as f:
                regels = f.readlines()
                laatsteRegel = regels[-1]
            
            assert "C~\tC?\tC?\t0\tblue\t2 - 2\n" in laatsteRegel


def test_writeHistory_illegal_input_graph():
    # testStartingFileIllegalGraph.json
    # {"n": 4, "starting-graph": "illegal", "red-graph": "illegal", "blue-graph": "illegal", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with pytest.raises(NetworkXError):
        writeHistory("testStartingFileIllegalGraph.json")


def test_writeHistory_illegal_input_intType():
    # testStartingFileIllegalIntType.json
    # {"n": "four", "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": "one", "starting-player": "one", "bias": "zero"}
    with pytest.raises(TypeError):
        writeHistory("testStartingFileIllegalIntType.json")

def test_writeHistory_illegal_input_intValue():
    # testStartingFileIllegalIntValue.json
    # {"n": -4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": -1, "starting-player": -1, "bias": -1}
    with pytest.raises(ValueError):
        writeHistory("testStartingFileIllegalIntValue.json")


def test_writeHistory_illegal_input_missing():
    # testStartingFileIllegalMissing.json
    # { "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with pytest.raises(KeyError):
        writeHistory("testStartingFileIllegalMissing.json")


def test_visualisationGraphs_missing_file():
    with pytest.raises(FileNotFoundError):
        writeHistory("/doesnot/exist.json")
