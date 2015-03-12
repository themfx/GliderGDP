#One script to rule them all...
#Laurence Jackson, lj8g10
# 30/01/2015 import data from active_aircraft.py
import time
from arraysum import arraysum
from P2_inflight_balance_calculation_v4 import inflight_stage,flight_balance
from coord_WP_dist import get_coords,WP_dist

"""UAV/glider flight parameters"""
from active_aircraft import m    # UAV/glider mass
from active_aircraft import g    # gravitational constant
from active_aircraft import C_D  # total drag coefficient
from active_aircraft import C_L  # Cruise lift coefficient

"""Flight Route input by pilot"""

coords = get_coords("long_WP.txt")

h_route,d_route = WP_dist(coords)

N = len(h_route)


#----------------------------------------------------------------------#



x = 150000                      #ground distance covered since starting
z = 200                         #current altitude
d_WP = 30                       #distance to next WP (taken from UAV)
float(d_WP)
WP_target = 2                   #Next WP ID number (taken from UAV)

"""Flight Balance for current altitude and distance travelled along flight path"""
"""
while x < arraysum(d_route,N):
    flight_balance(z,d_WP,WP_target,N,h_route,d_route)
    time.sleep(5)
    z = cs.alt()
    d_WP = cs.distnextWP
    WP_target = cs.nextWP
"""
flight_balance(z,d_WP,WP_target,N,h_route,d_route)
