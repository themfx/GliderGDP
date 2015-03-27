# --- Laurence Jackson, lj8g10 ---
# Core energy balance calculations.

from active_aircraft import *
import ASG.ArtSoar
from __main__ import SoarQ
from MissionTracking import printASG
from ArduParam import RelativeAlt

def inflight_stage(hA,hB,dAB,LD_ratio):
	"""
	Takes current altitude (hA), next WP altitude (hB), distance
	to next WP (dAB) and an L/D ratio and calculates whether more
	energy is required."""

	delta_h_ideal = (1/LD_ratio)*dAB
	ideal_alt = hB + delta_h_ideal

	if hA < ideal_alt:
		delta_h_diff = ideal_alt - hA
		E_req_AB = m*g*delta_h_diff
        
		printASG("More energy required!")
		printASG("Additional alt required en route = %.1f m"
					%delta_h_diff)
		printASG("Additional energy required en route = %.1f J"
					%E_req_AB)

		if hA+delta_h_diff < SF*hmax:
			printASG("Now soaring %.1f m" % delta_h_diff)
			SoarQ.put(delta_h_diff) # send soar request

		elif hA+delta_h_diff > SF*hmax and hA > hmin:
			printASG("Soaring now would exceed altitude ceiling")
			printASG("Continuing on glide for now...")

		elif hA+delta_h_diff > SF*hmax and hA < hmin:
			printASG("WARNING!! Dropping below min altitude!!")
			printASG("Climbing to %.1f m altitude" % (SF*hmax))
			SoarQ.put(SF*hmax-hA) # send soar request
        
	else:
		E_req_AB = 0
		printASG("No additional alt required to reach next WP")
		printASG("No additional energy required")
	pass

def flight_balance(z,d_WP,WP_target,N,h_route,d_route,LD_ratio):
	"""
	Prints feedback on whether energy is required to reach next
	WP."""
	i = WP_target
	printASG("You are at Stage %d: WP%d -> WP%d"%(i,i,i+1))
	printASG("Distance to WP%d is %.3f m (alt=%.1f//%.1fm)"
				%(i+1,d_WP,RelativeAlt(),h_route[i+1]))
	inflight_stage(z,h_route[i+1],d_WP,LD_ratio)
	pass
