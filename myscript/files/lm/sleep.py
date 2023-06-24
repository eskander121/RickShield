#!/usr/bin/env python3
from time import sleep
import subprocess
# this script is triggered by lm.py

# locks pc
subprocess.run("python3 uy.py", shell=True)
sleep (1)
# suspend pc 
subprocess.run("sudo -k pm-suspend", shell=True)
# command that takes picture of person 
subprocess.run("howdy snapshot", shell=True)
# run multiple script at the same time 
# b.py plays rickroll
# x.py keeps sound 100%
# hj.py enables startup program to run sleep.py after startup 
subprocess.run("python3 b.py & python3 x.py & python3 hj.py", shell=True)

  


