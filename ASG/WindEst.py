# --- Andy Ure, au4g10 ---
# Provide a wind estimate to energy calculation

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
	# Would be nice to get a more accurate wind estimate as
	#  we go along, like MAVProxy gives.
	pass

