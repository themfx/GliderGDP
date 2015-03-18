from ArduParam import * # use FetchParam and ChangeParam
from __main__ import v
import time
from MissionTracking import printASG

# remove these
import math
#from ASG.coord_WP_dist import get_coords
from ModernCoords import GetWPs
coords = GetWPs() #get_coords("/home/andy/ardupilot/ArduPlane/ASG_WP.txt")
Vmin = FetchParam(['ARSPD_FBW_MIN'])[0]*0.5

# Define an exception that specifically requests panic mode
class PanicPanic(Exception):pass

# A function to enter panic mode
def Enter():
	# First change the mode to RTL
	ChangeParam(['MODE'],['RTL'])
	ResetAll()
	printASG("EnterPanicMode complete")
	pass

# Check the current state, do we need to invoke a panic?
def Check(VL=Vmin,pL=15,pL_=-10,rL=30,vzL_=-20,aL=112,aL_=5): #correct PL_!!
	# Get current vehicle data
	p = v.attitude.pitch
	vz= v.velocity[2] 			# catch sharp dives
	r = abs(v.attitude.roll)	# use absolute value
	a = RelativeAlt()
	V = v.airspeed
	#[latT,lonT,z] = coords[v.commands.next] 	# we only care about z here - why do we :/

	AttNames = ['airspeed','pitch (+ve)','pitch (-ve)','roll','velocity (z)','alt (max)','alt (min)']
	AttCurrent = [-V,p,-p,r,-vz,a,-a]
	AttLimit = [-VL,pL,-pL_,rL,-vzL_,aL,-aL_]

	for (name,cur,lim) in zip(AttNames,AttCurrent,AttLimit):
		if cur>lim:
			raise PanicPanic, "Outside operation: %s=%.2f" %(name,cur)
	printASG("Panic check is all okay")
	pass

def VehicleMonitor(alert,t=0.2):
	while alert.empty():
		zero = time.time()
		Check()
		wait = t - (time.time() - zero)
		if wait>0:
			time.sleep(wait)
	printASG("VehicleMonitor detected alert, terminating")
	pass
