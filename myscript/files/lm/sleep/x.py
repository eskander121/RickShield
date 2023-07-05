import subprocess
from time import sleep
# this script is trigered by sleep.py

# unmutes sound
subprocess.run("amixer -D pulse set Master 1+ unmute -q", shell=True)
sleep(1)
# sets volume to 100%
subprocess.run("pactl -- set-sink-volume 0 150%", shell=True)
sleep(1)
# repeats this script
subprocess.run("python3 x.py", shell=True)


