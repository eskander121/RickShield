# Open the config file in an editor

# Import required modules
import os
import subprocess
import sys
# Check if we have rootish rights
# This is this far down the file so running the command for help is always possible
if os.getenv("SUDO_USER") is None:
	print("Please run this command as root:\n")
	print("\tsudo howdy " + " ".join(sys.argv[1:]))
	sys.exit(1)

# Let the user know what we're doing
print("Opening config.ini in the default editor")

# Default to the nano editor
editor = "/bin/nano"

# Use the user preferred editor if available
if "EDITOR" in os.environ:
	editor = os.environ["EDITOR"]
elif os.path.isfile("/etc/alternatives/editor"):
	editor = "/etc/alternatives/editor"

# Open the editor as a subprocess and fork it
subprocess.call([editor, os.path.dirname(os.path.realpath(__file__)) + "/../config.ini"])
