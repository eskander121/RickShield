import subprocess
from time import sleep
# this script is trigered by sleep.py

# unmutes sound
amixer -D pulse sset Master 150% unmute -q
# repeats this script
subprocess.run("python3 x.py", shell=True)


