from time import sleep
import subprocess
import getpass
username = getpass.getuser()
subprocess.run("sudo mv '~/.config/autostart/k.desktop' ~/.config/autostart ", shell=True)
