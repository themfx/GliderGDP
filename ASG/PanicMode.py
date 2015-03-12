from ArduParam import * # use FetchParam and ChangeParam
from __main__ import v
import time

# remove these
import math
from ASG.TidyCode.coord_WP_dist import get_coords
coords = get_coords("/home/andy/ardupilot/ArduPlane/ASG_WP.txt")
Vmin = FetchParam(['ARSPD_FBW_MIN'])[0]*0.8

# Define an exception that specifically requests panic mode
class PanicPanic(Exception):pass

# A function to enter panic mode
def Enter():
	# First change the mode to RTL
	ChangeParam(['MODE'],['RTL'])
	ResetAll()
	print("EnterPanicMode complete")
	pass

# Check the current state, do we need to invoke a panic?
def Check(VL=Vmin,pL=20,pL_=-20,rL=30,vzL_=-20,aL=5): #correct PL_!!
	# Get current vehicle data
	p = v.attitude.pitch
	vz= v.velocity[2]
	r = abs(v.attitude.roll)	# use absolute value
	a = RelativeAlt()
	V = v.airspeed
	print(v.wind.speed)
	[latT,lonT,z] = coords[v.commands.next]

	AttNames = ['airspeed','pitch (+ve)','pitch -ve','roll','velocity (z)','altitude']
	AttCurrent = [-V,p,-p,r,-vz,-a]
	AttLimit = [-VL,pL,-pL_,rL,-vzL_,-aL]

	for (name,cur,lim) in zip(AttNames,AttCurrent,AttLimit):
		if cur>lim:
			raise PanicPanic, "Outside operation: %s=%.2f" %(name,cur)
	print("Panic check is all okay") 	# may supress this
	pass

def VehicleMonitor(alert,t=0.5):
	while alert.empty():
		zero = time.time()
		Check()
		wait = t - (time.time() - zero)
		if wait>0:
			time.sleep(wait)
	print("VehicleMonitor detected alert, terminating")
	pass
