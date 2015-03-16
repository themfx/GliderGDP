#In-flight energy balance
#Laurence Jackson, lj8g10
# 30/01/2015 read data from active_aircraft.py
#--------------------------------------------------------------------#
#
#where:     hA is current altitude
#           hB is next WP altitude
#           dAB is distance to next WP

from active_aircraft import * #!# aju - tidy
import ASG.ArtSoar
from __main__ import SoarQ
from MissionTracking import printASG

def inflight_stage(hA,hB,dAB,LD_ratio):

    delta_h_ideal = (1/LD_ratio)*dAB           #ideal altitude change from current position
                                            #to target WP based on ideal glide slope

    ideal_alt = hB + delta_h_ideal          #ideal altitude

    if hA < ideal_alt:

        delta_h_diff = ideal_alt - hA

        E_req_AB = m*g*delta_h_diff
        
        printASG("More energy required!")
        printASG("Additional alt required en route = %.3f m" % delta_h_diff)
        printASG("Additional energy required en route = %.3f J" % E_req_AB)

        if hA+delta_h_diff < SF*hmax:

            printASG("\nNow soaring %.3f m" % delta_h_diff)
	    SoarQ.put(delta_h_diff)

        elif hA+delta_h_diff > SF*hmax and hA > hmin:

            printASG("\nSoaring now would exceed altitude ceiling")
            printASG("Continuing on glide for now...")

        elif hA+delta_h_diff > SF*hmax and hA < hmin:

            printASG("\nWARNING!! Dropping below minimum altitude!!")
            printASG("Climbing to %.3f m altitude" % (SF*hmax))
	    SoarQ.put(SF*hmax-hA)
        
    else:

        E_req_AB = 0
        
        printASG("No additional alt required to reach next WP")
        printASG("No additional energy required to reach next WP")
	pass

def flight_balance(z,d_WP,WP_target,N,h_route,d_route,LD_ratio):
    for i in range(N):
        if i+1 == WP_target and d_WP != 0:
            printASG("\n\nYou are at Stage %d: WP%d -> WP%d" %(i,i,i+1))
            printASG("Distance to WP%d is %.3f m (@ alt=%.1fm)" %(i+1,d_WP,h_route[i+1]))
            inflight_stage(z,h_route[i+1],d_WP,LD_ratio)
        elif i+1 == WP_target and d_WP == 0 and WP_target+1 < N+1:
            printASG("You are at WP%d" %(WP_target))
            printASG("Distance to WP%d is %.3f m" %(WP_target+1,d_route[i]))
        elif i+1 == WP_target and WP_target == N and d_WP == 0:
            printASG("You are at final WP: WP%d" %(N))


