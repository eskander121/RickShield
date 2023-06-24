from time import sleep
import subprocess
import getpass 

username = getpass.getuser()

# moves the startup file to place off choise to disable the sleep.py on startup
subprocess.run(" mv '/home/" + username + "/.config/autostart/k.desktop' '/home/" + username + "/Documents'", shell=True)
