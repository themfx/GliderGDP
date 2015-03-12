from __main__ import v, SoarQ
from ArduParam import *
from droneapi.lib import Location
from ASG.TidyCode.coord_WP_dist import get_coords
#VEHICLE MODE
import math,time

coords = get_coords("/home/andy/ardupilot/ArduPlane/ASG_WP.txt")

def Wait(alert,tSoar=2,tHead=0.4):
	"""
	Monitors the SoarQ queue for commands to soar. Should loop
	every tSoar seconds when waiting for soar command and updates,
	then every tHead seconds when waiting for a good heading to
	leave the loiter."""
	alt = 0 		# why is this here??
	t = tSoar 		# start by looping every tSoar seconds
	Soar = False 	# we're not soaring to begin with
	while alert.empty():
		start = time.time()
		if not SoarQ.empty():
			Soar = True
			altSoar = v.location.alt + SoarQ.get() #changed from RelativeAlt()
			if altSoar>alt:
				alt = altSoar
				if FetchParam(['MODE'])[0] != 'GUIDED':
					SetParam(['THR_MAX'],[75])
					lat = v.location.lat
					lon = v.location.lon
					v.commands.goto(Location(lat,lon,alt))
				else:
					v.commands.goto(Location(lat,lon,alt))
		elif (Soar==True) and (FetchParam(['THR_MAX'])[0] != 0):
			t = tHead
			if InHeading():
				SetParam(['MODE','THR_MAX'],['AUTO',0])
				alt = 0
				t = tSoar
				Soar = False
		wait = t - (time.time()-start)
		if wait>0:
			time.sleep(wait) 	# if executed fast enough, sleep for a while
	pass
				
def InHeading(tol=20):
	"""
	Checks the UAV is facing towards the next waypoint, so as it
	can exit it's loiter cleanly."""
	gc = math.degrees(v.attitude.yaw) 	# default yaw output is in radians

	[latT,lonT,z] = coords[v.commands.next]
	head = math.degrees(math.atan2(lonT-v.location.lon,latT-v.location.lat))

	# Define heading window to fall between
	hU= head + tol
	hL= head - tol

	if tan_(hU)>tan_(hL):
                if (tan_(gc)<tan_(hL)) or (tan_(gc)>tan_(hU)):
			return False
	else:
		if (tan_(gc)<tan_(hL)) and (tan_(gc)>tan_(hU)):
			return False
	print("Good heading identified")
	return True

def tan_(a):
	if a%360.==0:
		a+=1e-6		# avoid asymptotes
	a = math.radians(a)
	return math.tan(0.5*(a-math.pi))
