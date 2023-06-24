# Clear all models by deleting the whole file

# Import required modules
import os
import sys
import builtins

# Check if we have rootish rights
# This is this far down the file so running the command for help is always possible
if os.getenv("SUDO_USER") is None:
	print("Please run this command as root:\n")
	print("\tsudo howdy " + " ".join(sys.argv[1:]))
	sys.exit(1)

# Get the full path to this file
path = os.path.dirname(os.path.abspath(__file__))
# Get the passed user
user = builtins.howdy_user

# Check if the models folder is there
if not os.path.exists(path + "/../models"):
	print("No models created yet, can't clear them if they don't exist")
	sys.exit(1)

# Check if the user has a models file to delete
if not os.path.isfile(path + "/../models/" + user + ".dat"):
	print(user + " has no models or they have been cleared already")
	sys.exit(1)

# Only ask the user if there's no -y flag
if not builtins.howdy_args.y:
	# Double check with the user
	print("This will clear all models for " + user)
	ans = input("Do you want to continue [y/N]: ")

	# Abort if they don't answer y or Y
	if (ans.lower() != "y"):
		print('\nInerpeting as a "NO"')
		sys.exit(1)

# Delete otherwise
os.remove(path + "/../models/" + user + ".dat")
print("\nModels cleared")
