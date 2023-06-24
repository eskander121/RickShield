from time import sleep
import subprocess
from playsound import playsound
# this script is trigered by sleep.py

# waiting for authentication to be finished
sleep (5)
# playing the rickroll
playsound('KGzngdVKbrk_Rick-Astley---Never-Gonna-Give-You-Up.wav')
# repeating the song 
subprocess.run("python3 b.py", shell=True)
