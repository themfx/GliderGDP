#One script to rule them all...
#Laurence Jackson, lj8g10

import time

from P1_preflight_energy_calculation import preflight_stage,total_flight_energy
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

RouteStage = range(1,N)

#Reverse order for back calculation:

RouteStage.reverse()
d_route.reverse()
h_route.reverse()


#----------------------------------------------------------------------#


"""Total flight energy required stage by stage based on current flight path"""

total_flight_energy(RouteStage,h_route,d_route)


   
