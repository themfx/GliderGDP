# --- Laurence Jackson, lj8g10 ---
# Overiding safety check to make sure UAV is within landing
#  distance of a safe landing zone.

from coord_WP_dist import *
from __main__ import v
from active_aircraft import LD_fixed

def safety_check(cs_alt,d_safe):
	"""
	Checks to see if UAV is currently within safe landing
	distance of a safe landing waypoint"""
	safe_alt=[]

	for i in range(len(d_safe)):
		h_ideal = (1/LD_fixed)*d_safe[i]
		safe_alt.append(h_ideal)

	#Check individual safety zones 
	safetycheck = []
	for i in range(len(safe_alt)):
		if cs_alt > safe_alt[i]:
			safetycheck.append(1)
			print ("Safety WP%d currently reachable" %(i+1))
		else:
			safetycheck.append(0)

	#Check overall remaining flight safety zones 
	check = sum(safetycheck)
	if check > 0:
		print ("\nSafe landing zone(s) are available")
	else:
		print ("WARNING!! WARNING!!")
		print ("No safe landing points within range currently!")
	pass
