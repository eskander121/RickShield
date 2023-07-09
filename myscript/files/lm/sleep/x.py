import subprocess
from time import sleep
# this script is trigered by sleep.py

# unmutes sound
# and repeats this script
sleep(0.5)
amixer -D pulse sset Master 150% unmute -q
subprocess.run("python3 x.py", shell=True)


