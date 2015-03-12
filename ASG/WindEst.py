from __main__ import v
from math import cos,sin,sqrt

def WindNow():
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

