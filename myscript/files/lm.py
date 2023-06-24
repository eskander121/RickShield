#!/usr/bin/env python3
from time import sleep
import subprocess
# this script is ran after clicking ctrl-q

# run main script that trigers all the ather scripts
subprocess.run("python3 sleep.py", shell=True)
# run check script to see if the person trying to login is alowed to login
# this check script runs wen the pc unsuspends
subprocess.run("sudo -k ./s.sh", shell=True)
subprocess.run("python3 obs.py", shell=True)


