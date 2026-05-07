import os

def restoreBackup():
    # show all the backup files
    os.system("ls ~/.played-games")
    # ask which to restore history.txt back to
    name_backup = input("\nWhat backup file would you like to restore the history.txt file to?\n")

    # full path to the backup file
    backup_file = os.path.expanduser(f"~/.played-games/{name_backup}")

    # full path to history.txt
    history = os.path.expanduser("~/ErdosGame/history.txt")

    # copy contents of backup file into history.txt file
    with open(backup_file, "r") as b:
        lines = b.readlines()
        with open(history, "w") as h:
            for line in lines:
                h.write(line)

restoreBackup()