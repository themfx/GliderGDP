# Import necessary modules
from __main__ import v, SoarQ
from ArduParam import *
from droneapi.lib import Location
from coord_WP_dist import WP_dist#,get_coords
from ModernCoords import GetWPs
import math,time
from MissionTracking import printASG

coords = GetWPs()

def Wait(alert,tSoar=1,tHead=0.3):
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
			#Soar = True
			altSoar = RelativeAlt() + SoarQ.get() #changed back to v.location.alt
			if altSoar>alt:
				alt = altSoar
				if Soar != True:
					Soar = True
					SetParam(['THR_MAX'],[75])
					[lat,lon] = Centre()
					v.commands.goto(Location(lat,lon,alt))
				else:
					v.commands.goto(Location(lat,lon,alt))
		elif (Soar==True) and (RelativeAlt()>=0.9*alt):
			t = tHead
			NextWP_ = v.commands[v.commands.next]
			NextWP = [NextWP_.x,NextWP_.y,NextWP_.z]
			WPinLoiter = WP_dist([[lat,lon,alt],NextWP])[0][0] < 1.5*FetchParam(['WP_LOITER_RAD'])[0]
			if InHeading() or WPinLoiter:
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
	can exit it's loiter cleanly. Works within a tolerance of 20
	degrees by default."""
	gc = v.attitude.yaw 	# default yaw output is in radians
	tol = degrees(tol)

	# Get the next waypoint and which direction it's in
	[latT,lonT,z] = coords[v.commands.next]
	head = math.atan2(lonT-v.location.lon,latT-v.location.lat)

	# Define heading window to fall between
	hU= head + tol
	hL= head - tol

	# Check for alignment
	if tan_(hU)>tan_(hL):
                if (tan_(gc)<tan_(hL)) or (tan_(gc)>tan_(hU)):
			return False
	else:
		if (tan_(gc)<tan_(hL)) and (tan_(gc)>tan_(hU)):
			return False
	printASG("Good heading identified")
	return True

def tan_(a):
	"""Custom tan function for use in InHeading(). Uses degrees
	and avoids asymptotes."""
	if a%360.==0:
		a+=1e-6				# avoid asymptotes
	return math.tan(0.5*(a-math.pi))

from math import sin, asin, cos, atan2, radians, degrees, pi
def Centre():
	"""
	Returns the coordinates [lat,lon] of a loiter centre such
	that the artificial soar can be entered and exitied cleanly.

	Original code written by WM, edited by AJU."""
	# http://stackoverflow.com/questions/7278094/moving-a-cllocation-by-x-meters/20241963#20241963
	lat00 = v.location.lat
	long00 = v.location.lon
	angle = v.attitude.yaw + pi/2
	distance = FetchParam(['WP_LOITER_RAD'])[0]

	rad_earth = 6371e3          # Earth's radius [google]
	rad_d = 1.0*distance/rad_earth  # Radial distance between points.
	lat0, long0 = map(radians, [lat00, long00])
	lat = asin(sin(lat0)*cos(rad_d) + cos(lat0)*sin(rad_d)*cos(angle))
	lon = long0 + atan2(sin(angle)*sin(rad_d)*cos(lat0),
                        cos(rad_d) - sin(lat0)*sin(lat))

	return [degrees(lat),degrees(lon)]
