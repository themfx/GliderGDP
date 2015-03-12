#In-flight energy balance
#Laurence Jackson, lj8g10
# 30/01/2015 read data from active_aircraft.py
#--------------------------------------------------------------------#
#Modified from: P1-single-stage-altitude.py#
#where:     hA is current altitude
#           hB is next WP altitude
#           dAB is distance to next WP
#           stage is current flight path stage


def inflight_stage(hA,hB,dAB):

    delta_h_ideal = (C_D/C_L)*dAB           #ideal altitude change from current position
                                            #to target WP based on ideal glide slope

    ideal_alt = hB + delta_h_ideal          #ideal altitude

    if hA < ideal_alt:

        delta_h_diff = ideal_alt - hA

        E_req_AB = m*g*delta_h_diff
        
        print ("More energy required!")
        print ("Additional alt required en route = %.3f m" % delta_h_diff)
        print ("Additional energy required en route = %.3f J" % E_req_AB)

        if hA+delta_h_diff < SF*hmax:

            print ("\nNow soaring %.3f m" % delta_h_diff)

        elif hA+delta_h_diff > SF*hmax and hA > hmin:

            print ("\nSoaring now would exceed altitude ceiling")
            print ("Continuing on glide for now...")

        elif hA+delta_h_diff > SF*hmax and hA < hmin:

            print ("\nWARNING!! Dropping below minimum altitude!!")
            print ("Climbing to %.3f m altitude" % (SF*hmax))
        
    else:

        E_req_AB = 0
        
        print ("No additional alt required to reach next WP")
        print ("No additional energy required to reach next WP")
        
#--------------------------------------------------------------------#



"""UAV/glider flight parameters"""
 
from active_aircraft import m    # UAV/glider mass
from active_aircraft import g    # gravitational constant
from active_aircraft import C_D  # total drag coefficient
from active_aircraft import C_L  # Cruise lift coefficient
from active_aircraft import hmax # Max flight ceiling
from active_aircraft import hmin # Min safe flight altitude
from active_aircraft import SF   # Safety factor

# Above could be acheived by "from active_aircraft import *" but didn't do it for clarity

"""Flight Route input by pilot"""
"""
N = 4                      #Number of waypoints, including start and finish

RouteStage = range(1,N)        #Route stages, e.g Stage 1: WP1 -> WP2
"""
#Distance between waypoints:
"""d1 = 100.
d2 = 200.
d3 = 80.
d4 = 0.

d_route = [d1, d2, d3, d4]      #Waypoint distances for entire route
"""
#Altitude limits for each waypoint:
"""h1 = 150.                      
h2 = 100.                      
h3 = 95.
h4 = 50.

h_route = [h1, h2, h3, h4]      #Height constraints at each waypoint
"""
"""Flight Energy calculation"""


#Position along flight path calculation:

from arraysum import arraysum
"""
x = 120                     #Current ground distance covered during flight
float(x)
z = 70                      #Current altitude
float(z)
"""
def flight_balance(z,d_WP,WP_target,N,h_route,d_route):


    for i in range(N):
        if i+1 == WP_target and d_WP != 0:
            print ("You are at Stage %d: WP%d -> WP%d" %(i,i,i+1))
            print ("Distance to WP%d is %.3f m" %(i+1,d_WP))
            inflight_stage(z,h_route[i],d_WP)
        elif i+1 == WP_target and d_WP == 0 and WP_target+1 < N+1:
            print ("You are at WP%d" %(WP_target))
            print ("Distance to WP%d is %.3f m" %(WP_target+1,d_route[i]))
        elif i+1 == WP_target and WP_target == N and d_WP == 0:
            print ("You are at final WP: WP%d" %(N))

