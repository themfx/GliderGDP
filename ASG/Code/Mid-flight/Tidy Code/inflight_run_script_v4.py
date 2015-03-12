#One script to rule them all...
#Laurence Jackson, lj8g10
# 30/01/2015 import data from active_aircraft.py
import math
from inflight_balance_calculation_v5 import inflight_stage,flight_balance
from coord_WP_dist import get_coords,WP_dist
from wind_consideration import Opt_LD

"""UAV/glider flight parameters"""
from active_aircraft import m    # UAV/glider mass
from active_aircraft import g    # gravitational constant
from active_aircraft import hmax # Max flight ceiling
from active_aircraft import hmin # Min safe flight altitude
from active_aircraft import SF   # Safety factor
from active_aircraft import A    #V^2 coeff
from active_aircraft import B    #V coeff
from active_aircraft import C    #Constant

# Above could be acheived by "from active_aircraft import *" but didn't do it for clarity

"""Flight Route input by pilot"""

coords = get_coords("long_WP.txt")

h_route,d_route = WP_dist(coords)

N = len(h_route)


#----------------------------------------------------------------------#

# Values Read from the UAV autopilot while flying #

Vs =                         #vertical air mass velocity, +ve defined as rising air mass
Vw =                         #wind velocity component parallel to flight direction, +ve defined as head wind
z =                          #current altitude                   
d_WP =                       #distance to next waypoint
WP_target =                  #next waypoint reference number


#----------------------------------------------------------------------#

# Flight Balance is calculated #

LD_ratio = Opt_LD(Vw,Vs,A,B,C)

flight_balance(z,d_WP,WP_target,N,h_route,d_route,LD_ratio)






