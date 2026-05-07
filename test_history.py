import pytest
from startingConfigFile import writeHistory
from networkx import NetworkXError
import os
import json
from unittest.mock import patch
import time

def test_writeHistory():
    # testStartingFile.json
    # {"n": 4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with patch('os.system') as mock_system:
        writeHistory("testStartingFile.json")

        assert mock_system.call_count == 1
        aangeroepen_commando = mock_system.call_args[0]

        verwacht_commando_deel = "bash Erdos-Game-Generic.sh 4 C~ C? C? 1 1 0 >> pathToResult.txt"
            
        # Controleer of het commando de juiste parameters bevat
        assert verwacht_commando_deel in aangeroepen_commando
    
        # Controleert of het bestand bestaat
        assert os.path.exists("pathToResult.txt")
        # is de resultaat in pathToResult!!!!!!!!!!!!!!!

        with open("history", "r") as f:
            regels = f.readlines()
            laatsteRegel = regels[-1]
        
        assert "C~\tC?\tC?\t0\tblue\t2 - 2\n" in laatsteRegel


def test_writeHistory_foute_input_graaf():
    # testStartingFileOngeldigGraaf.json
    # {"n": 4, "starting-graph": "ongeldig", "red-graph": "ongeldig", "blue-graph": "ongeldig", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with pytest.raises(NetworkXError):
        writeHistory("testStartingFileOngeldigGraaf.json")


def test_writeHistory_foute_input_intType():
    # testStartingFileOngeldigInt.json
    # {"n": "vier", "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": "een", "starting-player": "een", "bias": "nul"}
    with pytest.raises(TypeError):
        writeHistory("testStartingFileOngeldigIntType.json")

def test_writeHistory_foute_input_intValue():
    # testStartingFileOngeldigIntValue.json
    # {"n": -4, "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": -1, "starting-player": -1, "bias": -1}
    with pytest.raises(ValueError):
        writeHistory("testStartingFileOngeldigIntValue.json")


def test_writeHistory_foute_input_missing():
    # testStartingFileOngeldigMissing.json
    # { "starting-graph": "C~", "red-graph": "C?", "blue-graph": "C?", "threadnumber": 1, "starting-player": 1, "bias": 0}
    with pytest.raises(KeyError):
        writeHistory("testStartingFileOngeldigMissing.json")


def test_visualisationGraphs_bestand_ontbreekt():
    with pytest.raises(FileNotFoundError):
        writeHistory("/bestaat/niet.json")


# moet de "om de uur" backup ook getest worden?????

os.system("python3 deletion")