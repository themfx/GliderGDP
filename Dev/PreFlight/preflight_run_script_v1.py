#One script to rule them all...
#Laurence Jackson, lj8g10
# 30/01/2015 import data from active_aircraft.py
import math
from preflight_energy_calculation_v4 import preflight_stage,total_flight_energy
from coord_WP_dist import get_coords,WP_dist

"""UAV/glider flight parameters"""
from active_aircraft import m    # UAV/glider mass
from active_aircraft import g    # gravitational constant
from active_aircraft import hmax # Max flight ceiling
from active_aircraft import hmin # Min safe flight altitude
from active_aircraft import SF   # Safety factor
from active_aircraft import A    #V^2 coeff
from active_aircraft import B    #V coeff
from active_aircraft import C    #Constant
from active_aircraft import LD_fixed #conservative L/D ratio approx.

# Above could be acheived by "from active_aircraft import *" but didn't do it for clarity

"""Flight Route input by pilot"""

coords = get_coords("long_WP.txt")

h_route,d_route = WP_dist(coords)

N = len(h_route)

RouteStage = range(1,N)

#----------------------------------------------------------------------#

# Assumed values, pre-flight #

Vs = 0                        #vertical air mass velocity, +ve defined as rising air mass
Vw = 0                        #wind velocity component parallel to flight direction, +ve defined as head wind


#----------------------------------------------------------------------#

# Flight Balance is calculated #


total_flight_energy(RouteStage,h_route,d_route,LD_fixed)






