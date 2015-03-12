#Pre-flight energy calculation
#Laurence Jackson, lj8g10

#--------------------------------------------------------------------#
#Taken from: P1-single-stage-altitude.py#

def preflight_stage(stage,hA,hB,dAB):

    print("stage: %d, hA = %.3f m, hB = %.3f m, dAB = %.3f m" %(stage,hA,hB,dAB))

    delta_h_min = (C_D/C_L)*dAB             #minimum height change such that B
                                            #can be reached from A without additional
                                            #altitude (energy) gains.

    delta_h = hA - hB                       #actual altitude change

    if delta_h < delta_h_min:

        delta_h_diff = delta_h_min - delta_h

        E_req_AB = m*g*delta_h_diff
        
        print ("More energy required: WP %d - WP %d" %(stage,stage+1))
        print ("Additional alt required en route = %.3f m" % delta_h_diff)
        print ("Additional energy required en route = %.3f J" % E_req_AB)
        
    else:

        E_req_AB = 0
        
        print ("No additional energy required: WP %d - WP %d" %(stage,stage+1))
        


    E_slope = m*g*delta_h_min           #E_slope energy required along ideal glide slope            

    if E_req_AB == 0:

        E_AB = E_slope
          
    else:

        E_AB = E_req_AB + E_slope

    return E_AB                         #E_AB is required stage energy from A -> B

#--------------------------------------------------------------------#



"""UAV/glider flight parameters"""

m = 20.                     #UAV/glider mass
g = 9.81                    #gravitational constant
C_D = 0.05                   #total drag coefficient
C_L = 1.5                   #Cruise lift coefficient

"""Flight Route input by pilot"""
"""
N = 4                      #Number of waypoints, including start and finish

RouteStage = range(1,N)        #Route stages, e.g Stage 1: WP1 -> WP2

#Distance between waypoints:
d1 = 100.
d2 = 200.
d3 = 80.
d4 = 0.

d_route = [d1, d2, d3, d4]      #Waypoint distances for entire route

#Altitude limits for each waypoint:
h1 = 150.                      
h2 = 100.                      
h3 = 95.
h4 = 50.

h_route = [h1, h2, h3, h4]      #Height constraints at each waypoint
"""
"""Flight Energy calculation"""
"""
#Working back from final stage:

RouteStage.reverse()           #reverse order for back calculation
d_route.reverse()           #reverse order for back calculation
h_route.reverse()           #reverse order for back calculation

flight_e = 0
"""

def total_flight_energy(RouteStage,h_route,d_route):
    flight_e = 0
    for i in RouteStage:
        E = preflight_stage(i,h_route[i],h_route[i-1],d_route[i])
        print("Stage Energy: %.3f J\n" %E)
        flight_e = flight_e + E


    # NOTE: total required flight energy will decrease as the flight continues,
    # because certain waypoints will have already been passed.

    print ("\nTotal flight energy required: %.3f J" % flight_e)



"""Features still to add:

- allow for predifned heights at waypoints and calculate flight energy
from there

"""


