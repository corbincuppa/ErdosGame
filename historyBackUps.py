import os
import time
import schedule
from startingConfigFile import *


def job():
    # full path to backup directory
    directory_backups = os.path.expanduser("~/.played-games")
    # if the directory doesn't exist yet, make it
    os.makedirs(directory_backups, exist_ok=True)
    # each backup shall have the name in the form of "history{time}" so 
    # each file has a  unique name
    directory_backups = os.path.join(directory_backups, f"history{round(time.time())}")
    
    # full path to git respository
    directory = os.path.expanduser("~/ErdosGame")
    # full path to history.txt file
    directory = os.path.join(directory, f"history.txt")

    # copy the contents of history.txt to the new backup file
    with open(directory, "r") as h:
        lines = h.readlines()
        with open(directory_backups, "a") as b:
            for line in lines:
                b.write(line)

# backup history file hourly
schedule.every(1).hours.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


