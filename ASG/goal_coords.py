# --- Wilhelm Munthe, wm4g10 ---
# Generating a WP location at a certain angle and distance from
#  another
from math import sin, asin, cos, atan2, radians

def new_coord(lat00, long00, angle, distance):
	"""
	Generates a WP location at a certain angle and distance from
	the original location. (E.g. used for artifical soar centre.
	"""
	# http://stackoverflow.com/questions/7278094/moving-a-
	#	cllocation-by-x-meters/20241963#20241963
	rad_earth = 6371e3          # Earth's radius [google]
	rad_d = 1.0*distance/rad_earth  # Radial distance between points.
	lat0, long0 = map(radians, [lat00, long00])
	lat = asin(sin(lat0)*cos(rad_d) + cos(lat0)*sin(rad_d)*cos(angle))
	lon = long0 + atan2(sin(angle)*sin(rad_d)*cos(lat0),
                        cos(rad_d) - sin(lat0)*sin(lat))
	return [lat,lon]
