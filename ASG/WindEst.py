from __main__ import v
from math import cos,sin,sqrt,radians
from active_aircraft import wVel,wDir

def SingleWind():
	"""
	Current solution for accounting for wind. Will take a wind
	velocity (vW in m/s) and a direction (vDir in deg from N)
	and will return the current wind relative to the UAV's
	current state."""
	wDir_ = radians(wDir) 	# convert wind direction to rad
	return wVel*cos(v.attitude.yaw-wDir_)


def WindNow():
	""" INCOMPLETE """
	# Grab what we need
	vel = v.velocity
	att = v.attitude
	air = v.airspeed

	GSP_ = [0,0,0]
	GPS_[0] = vel[0] * sin(att.yaw)
	GPS_[1] = vel[1] * cos(att.yaw)
	GPS_[2] = vel[2] * cos(att.pitch)

	GPS = sqrt(sum([vi**2 for vi in GPS_]))
	
	return [air,GPS,att]

