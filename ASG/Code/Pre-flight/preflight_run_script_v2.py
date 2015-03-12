#One script to rule them all...
#Laurence Jackson, lj8g10

import time

from P1_preflight_energy_calculation import preflight_stage,total_flight_energy
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

RouteStage = range(1,N)

#Reverse order for back calculation:

RouteStage.reverse()
d_route.reverse()
h_route.reverse()


#----------------------------------------------------------------------#


"""Total flight energy required stage by stage based on current flight path"""

total_flight_energy(RouteStage,h_route,d_route)


   
