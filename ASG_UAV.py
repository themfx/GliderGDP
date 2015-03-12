# Module to run ASG modules
from time import sleep

# Create a mavlink connection to our vehicle
print("Trying to connect to vehicle")
try:
	import __main__
	__main__.v = local_connect().get_vehicles()[0]
except:
	print("Failed in connection to vehicle, raising exception")
	raise
print("Vehicle connection established")


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
from ASG import UAVTest
print("Imported required run module, executing in 2s")
sleep(2)
UAVTest.F1()
