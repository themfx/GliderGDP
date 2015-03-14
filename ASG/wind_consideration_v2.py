#Laurence Jackson, lj8g10

#Wind consideration code:

import math

#This code uses the glide polar for the UAV (obtained through
#wind tunnel testing) to calculate current L/D ratio accounting
#for the effects of head/tailwinds and sink/rising air mass.

#The solutions/equations used below were obtained analytically.

#Note: positive Vw is defined as a headwind
#      positive Vs is defined as a sinking air mass

def Current_LD(V,Vw,Vs,A,B,C): 

    ##A,B,C are the glide polar Coefficients (quadratic relation)##

    Vv = (A*(V**2.))+(B*V)+C                 #sink rate as a function of airspeed

    grad = (Vv-Vs)/(V-Vw)               #gradient of line representing glide angle

    LD_actual = 1/math.atan(-1.*grad)

    return LD_actual





    
