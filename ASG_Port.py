# Module to run ASG modules

# Create a mavlink connection to our vehicle
print("Trying to connect to vehicle")
try:
	import __main__
	__main__.v = local_connect().get_vehicles()[0]
except:
	print("Failed in connection to vehicle, raising exception")
	raise
print("Vehicle connection established")

# Download waypoints and set home altitude
print("Downloading waypoints and setting home altitude correction")
try:
	from __main__ import v
	v.commands.download()
	print("Waiting for download to verify")
	v.commands.wait_valid
	__main__.AltC = v.commands[0].z
except:
	print("Failed in download of waypoints, raising exception")
	raise
print("Waypoint download complete, __main__.AltC set")


# Ensure ASG modules can be loaded
print("Checking ASG module directory can be loaded")
import sys
dir_ASG = '/home/andy/sitl'	# module location

# If it's not already in sys.path, add it
if not any(dir_ASG in s for s in sys.path):
	print("Adding ASG directory to sys.path")
	sys.path.append(dir_ASG)
	print("Directory added")
else:
	print("ASG directory already exists")

# Import the relevant module
from ASG import ASG_FT1 #UAVTest,SafeWait
print("Imported required run module, executing in 2s")
#SafeWait.s(2)
#UAVTest.F1()
ASG_FT1.Run1()
