# Module to run ASG modules
from time import sleep

# Ensure ASG modules can be loaded
print("Checking ASG module directory can be loaded")
import sys,os
dir_ASG = os.getcwd()+'/GliderGDP'		# seems to work

# If it's not already in sys.path, add it
if not any(dir_ASG in s for s in sys.path):
	print("Adding ASG directory to sys.path")
	sys.path.append(dir_ASG)
	print("Directory added")
else:
	print("ASG directory already exists")

from ASG.MissionTracking import printASG# MissionTracking
#printASG = MissionTracking.printASG

# Create a mavlink connection to our vehicle
printASG("Trying to connect to vehicle")
try:
	import __main__
	__main__.v = local_connect().get_vehicles()[0]
except:
	printASG("Failed in connection to vehicle, raising exception")
	raise
printASG("Vehicle connection established")

# Download waypoints and set home altitude
printASG("Downloading waypoints and setting home altitude correction")
from __main__ import v
v.commands.download()
retry = 5
while retry>0:
	try:
		#from __main__ import v
		#printASG("here we go")
		#v.commands.download()
		printASG("Waiting for download to verify")
		#v.commands.wait_valid
		sleep(5) 	# just in case, avoids error
		__main__.AltC = v.commands[0].z
	except:
		retry -= 1
		printASG("Failed in download of waypoints (%d attempts left)" %retry)
		if retry==0:
			raise
		pass
	else:
		retry = 0
	#raise
printASG("Waypoint download complete, __main__.AltC set")

# Import the relevant module
from ASG import ASG_FT1
printASG("Imported required run module, executing in 2s")
sleep(2)
ASG_FT1.Run1()
