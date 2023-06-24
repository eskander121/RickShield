
from time import sleep
import subprocess
# authenticate with sudo if authenticated kill python to disable all the scripts exept s.sh
subprocess.run("sudo pkill python", shell=True)
