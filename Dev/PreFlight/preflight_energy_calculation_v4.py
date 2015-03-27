#Pre-flight energy calculation
#Laurence Jackson, lj8g10
# 30/01/2015 imports from active_aircraft.py

#--------------------------------------------------------------------#
#Taken from: P1-single-stage-altitude.py#

def preflight_stage(stage,hA,hB,dAB,LD_ratio):

    print("stage: %d, hA = %.3f m, hB = %.3f m, dAB = %.3f m" %(stage,hA,hB,dAB))

    delta_h_min = (1/LD_ratio)*dAB             #minimum height change such that B
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

    return E_AB,E_req_AB                #E_AB is required stage energy from A -> B

#--------------------------------------------------------------------#


def total_flight_energy(RouteStage,h_route,d_route,LD_ratio):
    flight_e = 0
    additional_e = 0
    for i in RouteStage:
        E,extra_E = preflight_stage(i,h_route[i],h_route[i-1],d_route[i],LD_ratio)
        print("Stage Energy: %.3f J\n" %E)
        flight_e = flight_e + E
        additional_e = additional_e + extra_E

    print ("\nTotal flight energy required: %.3f J" % flight_e)
    print ("\nAdditional energy required (thermal/battery) for flight: %.3f J" % additional_e)


