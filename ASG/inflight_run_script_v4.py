# --- Laurence Jackson, lj8g10 ---
# Main scripts to run energy balance checks.

import math
import time
from inflight_balance_calculation_v5 import inflight_stage
from inflight_balance_calculation_v5 import flight_balance
from coord_WP_dist import WP_dist
from ModernCoords import GetWPs
from wind_consideration_v2 import Current_LD
from MissionTracking import printASG
from active_aircraft import *
from __main__ import v
from ArduParam import RelativeAlt
from WindEst import SingleWind

coords = GetWPs()

def LoopMainRun(alert,t=2):
	"""
	Loop to check the energy balance every 't' seconds during a
	flight."""
	while alert.empty():
		start = time.time()
		MainRun()
		wait = t - (time.time()-start)
		if wait>0:
			time.sleep(wait)
	printASG("LoopMainRun detected an alarm, terminating")
	pass

def MainRun():
	"""
	Main check of energy balance."""
	h_route,d_route = WP_dist(coords)
	N = len(h_route)

	Vs = 0
	Vw =  SingleWind()
	z = RelativeAlt()
	WP_target = v.commands.next

	currentLoc = [v.location.lat,v.location.lon,z]

	d_WP = WP_dist([currentLoc,nextLoc])[1][0]

	# Flight Balance is calculated #
	LD_ratio = Current_LD(v.airspeed,Vw,Vs,A,B,C)
	flight_balance(z,d_WP,WP_target,N,h_route,d_route,LD_ratio)
    pass
