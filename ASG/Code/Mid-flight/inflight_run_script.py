#One script to rule them all...
#Laurence Jackson, lj8g10

import time
from arraysum import arraysum
from P2_inflight_balance_calculation import inflight_stage,flight_balance
from coord_WP_dist import get_coords,WP_dist

"""UAV/glider flight parameters"""

m = 20.                     #UAV/glider mass
g = 9.81                    #gravitational constant
C_D = 0.05                   #total drag coefficient
C_L = 1.5                   #Cruise lift coefficient

"""Flight Route input by pilot"""

coords = get_coords("long_WP.txt")

h_route,d_route = WP_dist(coords)

N = len(h_route)


#----------------------------------------------------------------------#



x = 150000                       #ground distance covered since starting
z = 200                #current altitude

"""Flight Balance for current altitude and distance travelled along flight path"""
"""
while x < arraysum(d_route,N):
    flight_balance(x,z,N,h_route,d_route)
    time.sleep(5)
    x = cs.ground distance covered
    z = cs.alt()
"""
flight_balance(x,z,N,h_route,d_route)


   
