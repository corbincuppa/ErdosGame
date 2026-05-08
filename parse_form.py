import sys
from startingConfigFile import makeJSONFile, writeHistory

order        = sys.argv[1]
startGraph   = sys.argv[2]
redGraph     = sys.argv[3]
blueGraph    = sys.argv[4]
threads      = sys.argv[5]
startPlayer  = sys.argv[6]
bias         = sys.argv[7]

makeJSONFile(order, startGraph, redGraph, blueGraph, threads, startPlayer, bias)
writeHistory("startingFile.json")