import os

def restoreBackup():
    name_backup = input("What backup file would you like to restore the history.txt file to?\n")

    # full path to the backup file
    backup_file = os.path.expanduser(f"~/.played-games/{name_backup}")

    # full path to history.txt
    history = os.path.expanduser("~/ErdosGame/history.txt")

    with open(backup_file, "r") as b:
        lines = b.readlines()
        with open(history, "w") as h:
            for line in lines:
                h.write(line)

restoreBackup()