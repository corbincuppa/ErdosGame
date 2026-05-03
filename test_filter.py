import pytest

def testParsedArguments():
    # assert that parsed arguments are the given arguments
    

    
    captured = pytest.capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"