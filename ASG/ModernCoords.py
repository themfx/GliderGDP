# New code to get waypoint information on the ODROID
from __main__ import v

def GetWPs():
	"""
	Instead of relying on a saved waypoint file, this pulls the
	waypoint information directly from the vehicle."""
	WP = []
	for i,w in enumerate(v.commands):
		WP.append([w.x,w.y,w.z])
	return WP
